import re
from typing import Dict, List

from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


class DocumentSplitter:
    HEADERS_TO_SPLIT = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
        ("####", "h4"),
    ]

    TARGET_MIN_TOKENS = 450
    TARGET_MAX_TOKENS = 900
    CHUNK_MAX_TOKENS = 1200
    CHUNK_MIN_TOKENS = 150

    _CJK_RE = re.compile(r"[\u4e00-\u9fff]")
    _LATIN_WORD_RE = re.compile(r"[A-Za-z0-9_]+")
    _SYMBOL_RE = re.compile(r"[^\w\s]")
    _CODE_FENCE_RE = re.compile(r"^\s*```")
    _TABLE_SEP_RE = re.compile(r"^\s*\|?[\-\:\s]+\|[\-\|\:\s]*$")

    def __init__(self):
        self.header_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.HEADERS_TO_SPLIT,
            strip_headers=False,
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
            ],
        )

    def split_documents(self, documents: List[Document]) -> List[Document]:
        all_splits: List[Document] = []
        for doc in documents:
            all_splits.extend(self.split_single(doc))
        return all_splits

    def split_single(self, doc: Document) -> List[Document]:
        if not self._is_markdown_doc(doc):
            return self.general_splitter.split_documents([doc])

        sections = self._split_to_sections(doc)
        chunks: List[Document] = []
        for section in sections:
            section_blocks = self._split_blocks(section.page_content)
            chunks.extend(self._pack_blocks(section_blocks, section.metadata))
        return self._merge_small_tail(chunks)

    def _is_markdown_doc(self, doc: Document) -> bool:
        metadata = doc.metadata or {}
        candidate_fields = [
            str(metadata.get("filename", "")),
            str(metadata.get("path", "")),
            str(metadata.get("source", "")),
        ]
        for value in candidate_fields:
            if value.lower().endswith(".md"):
                return True
        return False

    def _split_to_sections(self, doc: Document) -> List[Document]:
        try:
            sections = self.header_splitter.split_text(doc.page_content)
        except Exception:
            sections = []

        if not sections:
            return [Document(page_content=doc.page_content, metadata=dict(doc.metadata))]

        merged_sections: List[Document] = []
        for section in sections:
            metadata = dict(doc.metadata)
            metadata.update(section.metadata)
            merged_sections.append(Document(page_content=section.page_content, metadata=metadata))
        return merged_sections

    def _split_blocks(self, text: str) -> List[str]:
        lines = text.splitlines()
        blocks: List[str] = []
        buffer: List[str] = []
        in_code_block = False
        in_table_block = False

        def flush_buffer() -> None:
            if buffer:
                block = "\n".join(buffer).strip("\n")
                if block.strip():
                    blocks.append(block)
                buffer.clear()

        for line in lines:
            stripped = line.strip()
            is_blank = stripped == ""
            is_code_fence = bool(self._CODE_FENCE_RE.match(line))
            is_table_line = "|" in line and not is_blank
            is_table_sep = bool(self._TABLE_SEP_RE.match(line))

            if in_code_block:
                buffer.append(line)
                if is_code_fence:
                    in_code_block = False
                    flush_buffer()
                continue

            if is_code_fence:
                flush_buffer()
                in_code_block = True
                buffer.append(line)
                continue

            if in_table_block:
                if is_table_line or is_table_sep:
                    buffer.append(line)
                else:
                    in_table_block = False
                    flush_buffer()
                    if not is_blank:
                        buffer.append(line)
                continue

            if is_table_line and not in_code_block:
                flush_buffer()
                in_table_block = True
                buffer.append(line)
                continue

            if is_blank:
                flush_buffer()
                continue

            buffer.append(line)

        flush_buffer()
        return blocks

    def _pack_blocks(self, blocks: List[str], base_metadata: Dict) -> List[Document]:
        output: List[Document] = []
        current_blocks: List[str] = []
        current_tokens = 0

        def flush_current() -> None:
            nonlocal current_blocks, current_tokens
            if not current_blocks:
                return
            content = "\n\n".join(current_blocks).strip()
            if not content:
                current_blocks = []
                current_tokens = 0
                return
            metadata = dict(base_metadata)
            metadata["estimated_tokens"] = self._estimate_tokens(content)
            output.append(Document(page_content=content, metadata=metadata))
            current_blocks = []
            current_tokens = 0

        for block in blocks:
            block_tokens = self._estimate_tokens(block)

            if block_tokens > self.CHUNK_MAX_TOKENS:
                flush_current()
                metadata = dict(base_metadata)
                metadata["estimated_tokens"] = block_tokens
                metadata["oversized_block"] = True
                output.append(Document(page_content=block, metadata=metadata))
                continue

            if current_blocks and (current_tokens + block_tokens > self.CHUNK_MAX_TOKENS):
                flush_current()

            current_blocks.append(block)
            current_tokens += block_tokens

            if current_tokens >= self.TARGET_MAX_TOKENS:
                flush_current()

        flush_current()
        return output

    def _merge_small_tail(self, chunks: List[Document]) -> List[Document]:
        if len(chunks) < 2:
            return chunks

        tail = chunks[-1]
        tail_tokens = self._estimate_tokens(tail.page_content)
        if tail_tokens >= self.CHUNK_MIN_TOKENS:
            return chunks

        prev = chunks[-2]
        merged_content = f"{prev.page_content}\n\n{tail.page_content}".strip()
        merged_metadata = dict(prev.metadata)
        merged_metadata["estimated_tokens"] = self._estimate_tokens(merged_content)
        chunks[-2] = Document(page_content=merged_content, metadata=merged_metadata)
        return chunks[:-1]

    def _estimate_tokens(self, text: str) -> int:
        latin_words = len(self._LATIN_WORD_RE.findall(text))
        cjk_chars = len(self._CJK_RE.findall(text))
        symbols = len(self._SYMBOL_RE.findall(text))
        rough_tokens = latin_words + cjk_chars + (symbols // 4)
        return max(1, rough_tokens)

