import json
from pathlib import Path
from typing import Dict, List, Tuple

import faiss
import numpy as np


class VectorStore:
    def __init__(self, store_path: str):
        self.store_path = Path(store_path)
        self.index_path = self.store_path / "index.faiss"
        self.metadata_path = self.store_path / "metadata.json"

    def save(self, embeddings: np.ndarray, chunks: List[Dict[str, str]]) -> None:
        if embeddings.size == 0:
            raise ValueError("Embeddings vazios.")

        self.store_path.mkdir(parents=True, exist_ok=True)

        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)
        index.add(embeddings)

        faiss.write_index(index, str(self.index_path))

        with open(self.metadata_path, "w", encoding="utf-8") as file:
            json.dump(chunks, file, ensure_ascii=False, indent=2)

    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> List[Tuple[Dict[str, str], float]]:
        if not self.index_path.exists() or not self.metadata_path.exists():
            raise FileNotFoundError("indice vetorial nao encontrado.")

        index = faiss.read_index(str(self.index_path))

        with open(self.metadata_path, "r", encoding="utf-8") as file:
            chunks = json.load(file)

        scores, indices = index.search(query_embedding, top_k)

        results = []

        for position, score in zip(indices[0], scores[0]):
            if position == -1:
                continue

            results.append((chunks[position], float(score)))

        return results