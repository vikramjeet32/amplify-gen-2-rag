import streamlit as st
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from ollama import Client

st.title("Amplify Gen 2 Assistant (RAG)")

model = SentenceTransformer("all-MiniLM-L6-v2")
client = Client()

index = faiss.read_index("data/faiss_index/index.faiss")
with open("data/faiss_index/chunks.json") as f:
    chunks_data = json.load(f)

question = st.text_input("Ask a question about Amplify Gen 2:")

if question:
    question_vector = model.encode([question])
    D, I = index.search(np.array(question_vector), k=3)
    context = "\n".join([chunks_data[i]["text"] for i in I[0]])

    response = client.chat(model='mistral', messages=[
        {"role": "system", "content": "You are an assistant that answers based on Amplify Gen 2 documentation."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
    ])

    st.markdown("### Answer:")
    st.write(response["message"]["content"])