import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="give me the latest news about AI for today aslo meniotn the link to the source of the news",
)
# print("Response Text:\n", response.text)
print("\nToken Usage Metadata:")
print("Prompt Tokens:", response.usage_metadata.prompt_token_count)
print("Response Tokens:", response.usage_metadata.candidates_token_count)
print("Total Tokens:", response.usage_metadata.total_token_count)