import numpy as np
from typing import List


class VectorStore:
    def __init__(self, embeddings: List[List[float]], chunks: List[str]):
        self.embeddings = np.array(embeddings)
        self.chunks = chunks

    def cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query_embedding: List[float], top_k: int = 3):
        query = np.array(query_embedding)

        similarities = []
        for idx, emb in enumerate(self.embeddings):
            score = self.cosine_similarity(query, emb)
            similarities.append((score, idx))

        similarities.sort(reverse=True, key=lambda x: x[0])

        results = []
        for score, idx in similarities[:top_k]:
            results.append({
                "score": score,
                "text": self.chunks[idx]
            })

        return results
