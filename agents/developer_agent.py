import os
from google import genai
from dotenv import load_dotenv

from utils.prompts import generate_webpage_prompt

load_dotenv()

client = genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

def get_webpage_from_llm(design_brief: str) -> None:
    """
    Fetches sumamrise article and build webpage design idea using LLM.
    """
    
    webpage_builder_prompt = generate_webpage_prompt(design_brief)

    try:
        webpage_code = client.models.generate_content(
            model="gemini-2.5-flash-preview-04-17",
            contents=webpage_builder_prompt
        )

        return   {'response' : webpage_code.text, 
                'prompt_token' : webpage_code.usage_metadata.prompt_token_count,
                'response_token': webpage_code.usage_metadata.candidates_token_count,
                'total_token': webpage_code.usage_metadata.total_token_count}
        

    except Exception as e:
        print(f" Error: {e}")
