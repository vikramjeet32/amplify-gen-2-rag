from scraper.web_scraper import scrape_recursive
from utils.cleaner import clean_and_chunk_all
import os

if __name__ == "__main__":
    scrape_recursive("https://docs.amplify.aws/gen2/start/quickstart/", depth=2)
    print("Scraping complete.")

    clean_and_chunk_all()
    print("Chunking complete.")

    os.system("python embeddings/embedder.py")