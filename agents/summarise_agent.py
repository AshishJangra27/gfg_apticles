import os
from google import genai
from dotenv import load_dotenv

from utils.prompts import generate_clean_summary_prompt

load_dotenv()

client = genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

def get_clean_summary_from_llm(article_text: str) -> None:
    """
    Fetches an article from the given URL, scrapes its content, generates a clean summary prompt, and retrieves the summary using a language model.
    """
    
    clean_summary_prompt = generate_clean_summary_prompt(article_text)

    try:
        clean_summary = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=clean_summary_prompt
        )

        return {'response' : clean_summary.text.strip(), 
                'prompt_token' : clean_summary.usage_metadata.prompt_token_count,
                'response_token': clean_summary.usage_metadata.candidates_token_count,
                'total_token': clean_summary.usage_metadata.total_token_count}
        

    except Exception as e:
        print(f" Error: {e}")
