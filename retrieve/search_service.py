from typing import List, Set
import hashlib
import math

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_graph_retriever import GraphRetriever
from graph_retriever.strategies import Eager


class SearchService:
    def __init__(self, vector_store: Chroma, embeddings: Embeddings):
        self.vector_store = vector_store
        self.embeddings = embeddings

    def search(self, query: str, k: int = 1) -> List[Document]:
        return self.vector_store.similarity_search(query, k=k)

    def create_graph_retriever(self, k: int = 5, start_k: int = 1, max_depth: int = 2) -> GraphRetriever:
        edges = [
            # 文档内强边（高精度）
            ("doc_id", "doc_id"),
            # 同路径补边（高精度）
            ("path", "path"),
            # 跨文档弱边（需配合 source_type/source_repo 过滤）
            ("normalized_title", "normalized_title"),
        ]
        strategy = Eager(k=k, start_k=start_k, max_depth=max_depth)
        return GraphRetriever(
            store=self.vector_store,
            edges=edges,
            strategy=strategy,
        )

    def graph_search(self, query: str, k: int = 5) -> List[Document]:
        retriever = self.create_graph_retriever(k=k)
        return retriever.invoke(query)

    @staticmethod
    def _cosine(a: List[float], b: List[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a)) + 1e-12
        nb = math.sqrt(sum(y * y for y in b)) + 1e-12
        return dot / (na * nb)

    def _mmr_select(
        self,
        *,
        query: str,
        docs: List[Document],
        top_n: int,
        lambda_mult: float
    ) -> List[Document]:
        if not docs:
            return []
        if top_n >= len(docs):
            return docs

        query_embedding = self.embeddings.embed_query(query)
        doc_embeddings = self.embeddings.embed_documents([d.page_content for d in docs])

        selected = []
        remaining = list(range(len(docs)))

        # 先选和 query 最相关的一条
        first = max(
            remaining,
            key=lambda i: self._cosine(query_embedding, doc_embeddings[i])
        )
        selected.append(first)
        remaining.remove(first)

        while remaining and len(selected) < top_n:
            def mmr_score(i: int) -> float:
                rel = self._cosine(query_embedding, doc_embeddings[i])
                div = max(self._cosine(doc_embeddings[i], doc_embeddings[j]) for j in selected)
                return lambda_mult * rel - (1 - lambda_mult) * div

            best = max(remaining, key=mmr_score)
            selected.append(best)
            remaining.remove(best)

        return [docs[i] for i in selected]

    def hybrid_search(self, query: str, k: int = 5) -> List[Document]:
        candidate_k = max(30, k * 3)
        vector_results = self.search(query, k=candidate_k)
        try:
            graph_results = self.graph_search(query, k=candidate_k)
        except Exception:
            graph_results = []

        seen_hashes: Set[str] = set()
        candidates: List[Document] = []
        for doc in vector_results + graph_results:
            content_key = hashlib.sha1(doc.page_content.encode("utf-8")).hexdigest()
            if content_key not in seen_hashes:
                seen_hashes.add(content_key)
                candidates.append(doc)

        # MMR 重排：先广召回，再做相关性+多样性平衡
        return self._mmr_select(
            query=query,
            docs=candidates,
            top_n=k,
            lambda_mult=0.8,
        )

