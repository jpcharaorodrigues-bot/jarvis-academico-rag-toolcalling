from typing import Dict, List

from app.config import Config
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore


class Retriever:
    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore(Config.VECTOR_STORE_PATH)

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, str]]:
        query_embedding = self.embedder.embed_query(query)
        results = self.vector_store.search(query_embedding, top_k)

        documents = []

        for chunk, score in results:
            documents.append({
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "content": chunk["content"],
                "score": score
            })

        return documents
