### 📄 `README.md`

```markdown
# 🔍 Amplify Gen 2 RAG Assistant (Offline AI)

This project is a fully local **Retrieval-Augmented Generation (RAG)** system built to answer natural language questions about **AWS Amplify Gen 2** documentation. It uses **FAISS for vector search**, **sentence-transformers for embeddings**, and **Ollama** to run local large language models like **Mistral** or **Gemma** — all completely offline.

---

## 🚀 Why I Built This

I recently started working on AWS Amplify Gen 2 and realized that most AI models don’t have updated knowledge about it.  
At the same time, I was curious about **local LLMs** and **RAG architecture** — so I decided to combine the two and build this project from scratch.

---

## 🧩 Tech Stack

- **Python** – FastAPI, Streamlit, BeautifulSoup
- **FAISS** – Fast local vector search
- **Sentence Transformers** – MiniLM-L6-v2 for embeddings
- **Ollama** – Run local LLMs like `mistral` or `gemma`
- **No external API required** – Fully private and free

---

## 📦 Project Structure
```

amplify-gen-2-rag/
├── scraper/ # Scrapes Amplify Gen 2 docs
├── utils/ # Cleans and chunks scraped content
├── embeddings/ # Embeds and indexes chunks using FAISS
├── data/ # Stores all data (raw, chunks, FAISS)
├── api/ # FastAPI backend for querying
├── ui/ # Streamlit interface for user input
├── main.py # Orchestrates scraping, chunking, and embedding
├── requirements.txt # Python dependencies

````

---

## ⚙️ Setup Instructions

### 🖥️ 1. Clone the Repository

```bash
git clone https://github.com/your-username/amplify-gen-2-rag.git
cd amplify-gen-2-rag
````

### 🐍 2. Create a Virtual Environment

```bash
python -m venv .venv
# Activate venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 📦 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🛠️ How to Run the Project

### 🔎 1. Scrape and Process Docs

```bash
python main.py
```

This will:

- Scrape Amplify Gen 2 docs
- Clean + chunk the content
- Generate vector embeddings
- Store vectors in FAISS

### 🚀 2. Start the API Server

```bash
uvicorn api.app:app --reload
```

Visit the Swagger UI at:  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

Use the `/ask` endpoint to send questions.

### 🌐 3. (Optional) Run the Streamlit UI

```bash
streamlit run ui/app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## 🤖 Running the LLM with Ollama

### ✅ Step 1: Install Ollama

- Download from: https://ollama.com/download
- Works on macOS, Windows (via native or WSL), and Linux

### ✅ Step 2: Start Ollama

```bash
ollama serve
```

Then run your model (e.g. Mistral or Gemma):

```bash
ollama run mistral
```

> You can switch models by changing the `model=` name in `api/app.py`

---

## ⚠️ Known Limitations

- ❗ On low-spec systems, each query may take **5–6 minutes** due to large model size and no GPU acceleration.
- ℹ️ Reduce context size or switch to smaller models like `gemma:2b` for better performance.

---

## 🌟 Future Improvements

- Add GitHub issue scraping
- Add query history saving
- Add model selector toggle in UI
- Optimize chunk length + token budget

---

## 📬 Let's Connect

If you're working with local LLMs, self-hosted AI, or RAG systems — feel free to reach out or fork the project!
