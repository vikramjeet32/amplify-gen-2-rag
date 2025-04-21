# ---- api/app.py ----
from fastapi import FastAPI, Query
from pydantic import BaseModel
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from ollama import Client

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")
client = Client()

# Load FAISS index
index = faiss.read_index("data/faiss_index/index.faiss")
with open("data/faiss_index/chunks.json") as f:
    chunks_data = json.load(f)

class QueryInput(BaseModel):
    question: str

@app.post("/ask")
def ask_question(input: QueryInput):
    question = input.question
    question_vector = model.encode([question])
    D, I = index.search(np.array(question_vector), k=3)
    context = "\n".join([chunks_data[i]["text"] for i in I[0]])

    # Query local LLM (Mistral)
    response = client.chat(model='mistral', messages=[
        {"role": "system", "content": "You are an assistant that answers based on Amplify Gen 2 documentation."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
    ])

    return {"answer": response["message"]["content"]}
