from app.rag.chunker import TextChunker


def test_chunker_gera_chunks():
    chunker = TextChunker(chunk_size=3, overlap=1)

    documents = [
        {
            "source": "teste.txt",
            "content": "um dois tres quatro cinco seis"
        }
    ]

    chunks = chunker.chunk_documents(documents)

    assert len(chunks) == 3
    assert chunks[0]["source"] == "teste.txt"
    assert chunks[0]["chunk_id"] == "teste.txt_chunk_0"
