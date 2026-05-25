from app.config import Config
from app.rag.chunker import TextChunker
from app.rag.embedder import Embedder
from app.rag.loader import DocumentLoader
from app.rag.vector_store import VectorStore


class RagIndexer:
    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = TextChunker(
            chunk_size=Config.CHUNK_SIZE,
            overlap=Config.CHUNK_OVERLAP
        )
        self.embedder = Embedder()
        self.vector_store = VectorStore(Config.VECTOR_STORE_PATH)

    def build(self):
        documents = self.loader.load_documents(Config.DOCUMENTS_PATH)
        chunks = self.chunker.chunk_documents(documents)
        texts = [chunk["content"] for chunk in chunks]
        embeddings = self.embedder.embed_texts(texts)

        self.vector_store.save(embeddings, chunks)

        return {
            "documents": len(documents),
            "chunks": len(chunks)
        }
