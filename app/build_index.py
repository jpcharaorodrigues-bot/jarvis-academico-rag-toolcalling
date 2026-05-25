from app.rag.indexer import RagIndexer


def main():
    result = RagIndexer().build()

    print("Índice RAG criado.")
    print(f"Documentos: {result['documents']}")
    print(f"Chunks: {result['chunks']}")


if __name__ == "__main__":
    main()
