from typing import Dict, List


class TextChunker:
    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        if chunk_size <= 0:
            raise ValueError("chunk_size inválido.")

        if overlap < 0:
            raise ValueError("overlap inválido.")

        if overlap >= chunk_size:
            raise ValueError("overlap maior que chunk_size.")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_documents(self, documents: List[Dict[str, str]]) -> List[Dict[str, str]]:
        chunks = []

        for document in documents:
            source = document["source"]
            content = document["content"]

            for index, chunk in enumerate(self._chunk_text(content)):
                chunks.append({
                    "source": source,
                    "chunk_id": f"{source}_chunk_{index}",
                    "content": chunk
                })

        return chunks

    def _chunk_text(self, text: str) -> List[str]:
        words = text.split()

        if not words:
            return []

        chunks = []
        start = 0

        while start < len(words):
            end = start + self.chunk_size
            chunks.append(" ".join(words[start:end]))

            if end >= len(words):
                break

            start = end - self.overlap

        return chunks
