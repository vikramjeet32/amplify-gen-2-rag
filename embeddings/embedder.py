import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/processed_chunks.json") as f:
    data = json.load(f)

texts = [d["text"] for d in data]
embeddings = model.encode(texts)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, "data/faiss_index/index.faiss")

with open("data/faiss_index/chunks.json", "w") as f:
    json.dump(data, f)

print("Embedding and indexing complete.")