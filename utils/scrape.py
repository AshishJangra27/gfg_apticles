import os
import requests
from bs4 import BeautifulSoup
import html2text

def scrape_article(url: str, save: bool = False, output_dir: str = "./") -> str:
    """
    Scrapes the main content from a web article and returns it as markdown text.

    Parameters:
    - url: str → The URL of the article to scrape.
    - save: bool → Whether to save the scraped content to a markdown file.
    - output_dir: str → Directory to save the file if save=True.

    Returns:
    - str → The cleaned article text in markdown format.
    """

    headers = { 'User-Agent': 'Mozilla/5.0' }
    response = requests.get(url, headers=headers)
    
    if not response.ok:
        raise Exception(f"Failed to fetch article: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()
    
    article = soup.find('article')
    content = article if article else soup.body

    markdown_text = html2text.html2text(str(content)).strip()

    if save:
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "raw_article.md"), "w", encoding="utf-8") as f:
            f.write(markdown_text)

    return markdown_text
