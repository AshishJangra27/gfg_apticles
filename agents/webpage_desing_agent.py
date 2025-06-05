import os
from google import genai
from dotenv import load_dotenv

from utils.prompts import generate_webpage_design_prompt

load_dotenv()

client = genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

def get_webpage_design_from_llm(summarised_article: str) -> None:
    """
    Fetches sumamrise article and build webpage design idea using LLM.
    """
    
    webpage_design_prompt = generate_webpage_design_prompt(summarised_article)

    try:
        webpage_design_idea = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=webpage_design_prompt
        )

        return {'response' : webpage_design_idea.text.strip(), 
             'prompt_token' : webpage_design_idea.usage_metadata.prompt_token_count,
            'response_token': webpage_design_idea.usage_metadata.candidates_token_count,
            'total_token': webpage_design_idea.usage_metadata.total_token_count}
        

    except Exception as e:
        print(f" Error: {e}")
