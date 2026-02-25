from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


class DocumentSplitter:
    HEADERS_TO_SPLIT = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
        ("####", "h4"),
    ]

    def __init__(self):
        self.header_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.HEADERS_TO_SPLIT,
            strip_headers=False
        )
        self.general_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=[
                "\n\n",
                "\n",
                ". ",
                "。",
                "; ",
                "；",
                ", ",
                "，",
                " ",
                "",
            ]
        )

    def split_documents(self, documents: List[Document]) -> List[Document]:
        all_splits: List[Document] = []
        for doc in documents:
            chunks = self.split_single(doc)
            all_splits.extend(chunks)
        return all_splits

    def split_single(self, doc: Document) -> List[Document]:
        try:
            chunks = self.header_splitter.split_text(doc.page_content)
        except Exception:
            chunks = []
        if not chunks:
            return self.general_splitter.split_documents([doc])
        for chunk in chunks:
            chunk.metadata.update(doc.metadata)
        return chunks

