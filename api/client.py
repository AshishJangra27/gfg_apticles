import requests

api_url = "http://127.0.0.1:8000/generate-webpage"

payload = {
    "url": "https://www.geeksforgeeks.org/python-if-else/"
}

response = requests.post(api_url, json=payload)

if response.status_code == 200:
    result = response.json()
    print("✅ API Call Successful!")
    print("\n🔹 Summary:\n", result["summary"][:300], "...")
    print("\n🔹 Design Brief:\n", result["design"][:300], "...")
    print("\n🔹 HTML Snippet:\n", result["html"][:300], "...")
    print("\n📊 Tokens:\n", result["tokens"])
else:
    print(f"❌ Error {response.status_code}: {response.text}")
