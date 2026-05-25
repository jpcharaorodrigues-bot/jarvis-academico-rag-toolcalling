from typing import Dict, List


class TextChunker:
    """
    Divide documentos em chunks para recuperação no RAG.

    Estratégia:
    - chunk_size: número aproximado de palavras por chunk
    - overlap: quantidade de palavras repetidas entre chunks

    O overlap reduz perda de contexto entre divisões.
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        if chunk_size <= 0:
            raise ValueError("chunk_size deve ser maior que zero.")

        if overlap < 0:
            raise ValueError("overlap não pode ser negativo.")

        if overlap >= chunk_size:
            raise ValueError("overlap deve ser menor que chunk_size.")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_documents(self, documents: List[Dict[str, str]]) -> List[Dict[str, str]]:
        chunks = []

        for document in documents:
            source = document["source"]
            content = document["content"]

            document_chunks = self._chunk_text(content)

            for index, chunk in enumerate(document_chunks):
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
            chunk_words = words[start:end]

            chunks.append(" ".join(chunk_words))

            if end >= len(words):
                break

            start = end - self.overlap

        return chunks
