from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from utils.scrape import scrape_article
from agents.agents import (
    get_clean_summary_from_llm,
    get_webpage_design_from_llm,
    get_webpage_from_llm
)
from utils.support import llm_log, save_log, initialize_run

# Define request body schema
class ArticleInput(BaseModel):
    url: str

# Initialize FastAPI app
app = FastAPI(title="GFG Apticles API")

# CORS middleware (for frontends like Streamlit, React etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-webpage")
def generate_webpage(data: ArticleInput):
    
    url = data.url

    try:
        # Initialize run folder and logs
        run_folder, llm_logs = initialize_run(url)

        # Run the full pipeline
        raw_article = scrape_article(url, save=True, output_dir=run_folder)
        summarised_article = get_clean_summary_from_llm(raw_article, save=True, output_dir=run_folder)
        design_brief = get_webpage_design_from_llm(summarised_article['response'], save=True, output_dir=run_folder)
        webpage_code = get_webpage_from_llm(design_brief['response'], save=True, output_dir=run_folder)

        # Collect token usage
        llm_logs['summariser'] = llm_log(summarised_article)
        llm_logs['designer'] = llm_log(design_brief)
        llm_logs['developer'] = llm_log(webpage_code)

        # Save log
        save_log(llm_logs, run_folder)

        # Respond with all generated outputs
        return {
            "status": "success",
            "url": url,
            "run_folder": run_folder,
            "summary": summarised_article['response'],
            "design": design_brief['response'],
            "html": webpage_code['response'],
            "tokens": llm_logs
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
