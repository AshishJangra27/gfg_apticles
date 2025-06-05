import json
import os
from datetime import datetime
from utils.scrape import scrape_article
from agents.summarise_agent import get_clean_summary_from_llm
from agents.webpage_desing_agent import get_webpage_design_from_llm
from agents.developer_agent import get_webpage_from_llm

llm_logs = {}

def llm_log(agent_name, response_obj):
    llm_logs[agent_name] = {
        "prompt_token": response_obj['prompt_token'],
        "response_token": response_obj['response_token'],
        "total_token": response_obj['total_token']
    }

if __name__ == "__main__":

    # url = input("Enter article URL: ")
    url = 'https://www.geeksforgeeks.org/cosine-similarity/'
    llm_logs['timestamp'] = datetime.now().isoformat()
    llm_logs['url'] = url

    output_dir = "outputs/"
    os.mkfir(output_dir, exist_ok=True)

    try:
        raw_article = scrape_article(url)
        print("Article scraped successfully.\n")

        summarised_article = get_clean_summary_from_llm(raw_article)
        llm_log('summariser', summarised_article)
        print("Article summarised successfully.\n")

        design_brief = get_webpage_design_from_llm(summarised_article['response'])
        llm_log('designer', design_brief)
        print("Designed ideas successfully.\n")

        webpage_code = get_webpage_from_llm(design_brief['response'])
        llm_log('developer', webpage_code)
        print("Code generated successfully.\n")

        with open(os.path.join(output_dir, "article_summary.md"), "w", encoding="utf-8") as f:
            f.write(summarised_article['response'])

        with open(os.path.join(output_dir, "app_design.md"), "w", encoding="utf-8") as f:
            f.write(design_brief['response'])

        with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(webpage_code['response'])

        with open(os.path.join(output_dir, "token_report.json"), "w", encoding="utf-8") as f:
            json.dump(llm_logs, f, indent=4)

    except Exception as e:
        print(f"Error: {e}")
