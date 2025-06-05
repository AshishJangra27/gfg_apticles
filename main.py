import json
import os
from datetime import datetime
from utils.scrape import scrape_article
from agents.agents import get_clean_summary_from_llm,  get_webpage_design_from_llm,  get_webpage_from_llm
# from agents.webpage_desing_agent import get_webpage_design_from_llm
# from agents.developer_agent import get_webpage_from_llm
from utils.support import llm_log, save_log, initialize_run

llm_logs = {}

if __name__ == "__main__":

    url = input("Enter article URL: ")
    run_folder, llm_logs = initialize_run(url)

    try:
        
        raw_article = scrape_article(url, save=True, output_dir=run_folder)
        summarised_article = get_clean_summary_from_llm(raw_article, save=True, output_dir=run_folder)
        design_brief = get_webpage_design_from_llm(summarised_article['response'], save=True, output_dir=run_folder)
        webpage_code = get_webpage_from_llm(design_brief['response'], save=True, output_dir=run_folder)

        llm_logs['summariser'] = llm_log(summarised_article)
        llm_logs['designer'] = llm_log(design_brief)
        llm_logs['developer'] = llm_log(webpage_code)

        save_log(llm_logs, run_folder)

    except Exception as e:
        print(f"Error: {e}")