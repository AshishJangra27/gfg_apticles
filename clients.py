import requests
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import re

api_url = 'https://gfg-apticles-728938563934.asia-south1.run.app/generate-webpage'

urls = [
    "https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/",
    "https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/"
    "https://www.geeksforgeeks.org/introduction-to-binary-tree/",
    "https://www.geeksforgeeks.org/binary-search/",
    "https://www.geeksforgeeks.org/bubble-sort-algorithm/"
    "https://www.geeksforgeeks.org/decision-tree-introduction-example/",
    "https://www.geeksforgeeks.org/support-vector-machine-algorithm/",
    "https://www.geeksforgeeks.org/k-nearest-neighbours/",
    "https://www.geeksforgeeks.org/python-lists/"
]

def url_to_folder_name(url):
    slug = url.strip('/').split('/')[-1]
    return re.sub(r'[^\w\s-]', '', slug).strip().replace(' ', '_')

def process_url_variations(url):
    try:
        folder_name = url_to_folder_name(url)
        dir_path = Path("outputs") / folder_name
        dir_path.mkdir(parents=True, exist_ok=True)

        for i in range(5):
            r = requests.post(api_url, json={"url": url}, timeout=300)
            if not r.ok:
                return f"❌ {url} | {r.status_code} - {r.text}"

            data = r.json()
            html = data["html"][7:-3]
            (dir_path / f"v{i+1}.html").write_text(html, encoding='utf-8')

            if i == 0 and "tokens" in data:
                (dir_path / "tokens.json").write_text(
                    json.dumps(data["tokens"], indent=2), encoding='utf-8'
                )

        return f"✅ {url} | Saved v1-v3.html + tokens.json in '{folder_name}'"
    except Exception as e:
        return f"⚠️ {url} | {e}"

with ThreadPoolExecutor(max_workers=32) as executor:
    for result in executor.map(process_url_variations, urls):
        print(result)