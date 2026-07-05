import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_search(query, index_path, chunks, top_k=5):
    query_embedding = model.encode(
    [query],
    convert_to_numpy=True,
    normalize_embeddings=True
)

    index = faiss.read_index(index_path)

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i, distance in zip(indices[0], distances[0]):
        results.append({
            "chunk_id": chunks[i]["id"],
            "score": float(distance),
            "text": chunks[i]["text"]
        })

    return results

def retrieve_chunks(query, index_path, chunks, top_k=3):
    return semantic_search(query, index_path, chunks, top_k)
