import os
from google import genai
from dotenv import load_dotenv
from utils.prompts import generate_webpage_prompt, generate_webpage_design_prompt, generate_clean_summary_prompt

load_dotenv()
client = genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))



def get_clean_summary_from_llm(article_text: str, save: bool = False, output_dir: str = "./") -> dict:
    """
    Fetches an article summary using a language model.
    
    Parameters:
    - article_text: str → The content of the article to summarize.
    - save: bool → Whether to save the summary to a markdown file.
    - output_dir: str → Directory to save the summary file if save=True.
    
    Returns:
    - dict containing response, token usage info
    """
    
    clean_summary_prompt = generate_clean_summary_prompt(article_text)

    try:
        clean_summary = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=clean_summary_prompt
        )

        summarised_article = {
            'response': clean_summary.text.strip(),
            'prompt_token': clean_summary.usage_metadata.prompt_token_count,
            'response_token': clean_summary.usage_metadata.candidates_token_count,
            'total_token': clean_summary.usage_metadata.total_token_count
        }

        if save:
            os.makedirs(output_dir, exist_ok=True)
            with open(os.path.join(output_dir, "article_summary.md"), "w", encoding="utf-8") as f:
                f.write(summarised_article['response'])

        return summarised_article

    except Exception as e:
        print(f"Error: {e}")
        return {}








def get_webpage_design_from_llm(summarised_article: str, save: bool = False, output_dir: str = "./") -> dict:
    """
    Generates a webpage design idea using LLM from a summarised article.

    Parameters:
    - summarised_article: str → The input text summarizing an article.
    - save: bool → Whether to save the design idea to a markdown file.
    - output_dir: str → Directory to save the file if save=True.

    Returns:
    - dict containing response and token usage information
    """

    webpage_design_prompt = generate_webpage_design_prompt(summarised_article)

    try:
        webpage_design_idea = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=webpage_design_prompt
        )

        design_response = {
            'response': webpage_design_idea.text.strip(),
            'prompt_token': webpage_design_idea.usage_metadata.prompt_token_count,
            'response_token': webpage_design_idea.usage_metadata.candidates_token_count,
            'total_token': webpage_design_idea.usage_metadata.total_token_count
        }

        if save:
            os.makedirs(output_dir, exist_ok=True)
            with open(os.path.join(output_dir, "webpage_design_prompt.md"), "w", encoding="utf-8") as f:
                f.write(design_response['response'])

        return design_response

    except Exception as e:
        print(f"Error: {e}")
        return {}










def get_webpage_from_llm(design_brief: str, save: bool = False, output_dir: str = "./") -> dict:
    """
    Generates a complete webpage code from a design brief using LLM.

    Parameters:
    - design_brief: str → The textual description of the webpage design.
    - save: bool → Whether to save the generated webpage code to a file.
    - output_dir: str → Directory to save the file if save=True.

    Returns:
    - dict containing response and token usage information
    """

    webpage_builder_prompt = generate_webpage_prompt(design_brief)

    try:
        webpage_code = client.models.generate_content(
            model="gemini-2.5-flash-preview-04-17",
            contents=webpage_builder_prompt
        )

        code_response = {
            'response': webpage_code.text,
            'prompt_token': webpage_code.usage_metadata.prompt_token_count,
            'response_token': webpage_code.usage_metadata.candidates_token_count,
            'total_token': webpage_code.usage_metadata.total_token_count
        }

        if save:
            os.makedirs(output_dir, exist_ok=True)
            with open(os.path.join(output_dir, "webpage_code.html"), "w", encoding="utf-8") as f:
                f.write(code_response['response'])

            with open(os.path.join('', "index.html"), "w", encoding="utf-8") as f:
                f.write(code_response['response'])

        return code_response

    except Exception as e:
        print(f"Error: {e}")
        return {}