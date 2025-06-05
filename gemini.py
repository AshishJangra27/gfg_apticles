import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="give me the latest news about AI for today aslo meniotn the link to the source of the news",
)
print(response.text)