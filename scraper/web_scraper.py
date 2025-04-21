import requests
from bs4 import BeautifulSoup
from readability import Document
from urllib.parse import urljoin, urlparse
import os

visited = set()

BASE_URL = "https://docs.amplify.aws/gen2/start/quickstart/"


def is_valid(url, base):
    return urlparse(url).netloc in ['', urlparse(base).netloc]


def clean_html(html):
    doc = Document(html)
    soup = BeautifulSoup(doc.summary(), 'html.parser')
    return soup.get_text(separator="\n", strip=True)


def scrape_recursive(url, depth=2):
    if depth == 0 or url in visited:
        return []
    visited.add(url)
    try:
        res = requests.get(url)
        html = res.text
    except:
        return []

    content = clean_html(html)
    filename = os.path.join("data/raw_pages", urlparse(url).path.strip("/").replace("/", "_") + ".txt")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(content)

    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a', href=True):
        full_url = urljoin(url, link['href'])
        if is_valid(full_url, BASE_URL):
            scrape_recursive(full_url, depth - 1)