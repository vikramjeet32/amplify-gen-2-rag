import os
import json
import re
from pathlib import Path

CHUNK_SIZE = 500  # words

def clean_and_chunk_all(raw_dir="data/raw_pages", out_file="data/processed_chunks.json"):
    chunks = []
    for file in Path(raw_dir).rglob("*.txt"):
        with open(file, "r") as f:
            text = f.read()
        clean_text = re.sub(r'\s+', ' ', text).strip()
        chunked = chunk_text(clean_text, CHUNK_SIZE)
        for chunk in chunked:
            chunks.append({"source": str(file), "text": chunk})
    with open(out_file, "w") as f:
        json.dump(chunks, f)


def chunk_text(text, max_words):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]