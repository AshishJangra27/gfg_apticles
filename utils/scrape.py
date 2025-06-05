# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.geeksforgeeks.org/ml-linear-regression/'
# headers = { 'User-Agent': 'Mozilla/5.0' }

# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')

# article = soup.find('article')

# if article:
#     content_tags = article.find_all(['p', 'li', 'h1', 'h2', 'h3', 'pre', 'code'])

#     full_text = '\n\n'.join(tag.get_text(strip=True) for tag in content_tags)
#     print(full_text)
# else:
#     print("Article content not found.")


import requests
from bs4 import BeautifulSoup
import html2text

def scrape_article(url: str) -> str:
    headers = { 'User-Agent': 'Mozilla/5.0' }
    response = requests.get(url, headers=headers)
    
    if not response.ok:
        raise Exception(f"Failed to fetch article: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()
    
    article = soup.find('article')
    content = article if article else soup.body

    markdown_text = html2text.html2text(str(content))
    
    return markdown_text.strip()