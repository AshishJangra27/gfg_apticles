import os
import json
from datetime import datetime

def llm_log(response_obj):
    
    return {
        "prompt_token": response_obj['prompt_token'],
        "response_token": response_obj['response_token'],
        "total_token": response_obj['total_token']
        }

def save_log(log_data: dict, output_path: str) -> None:

    try:
        with open(output_path + '/logs.json', "w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=4)
    except Exception as e:
        print(f"Failed to save logs: {e}")


def initialize_run(url) -> tuple:

    timestamp = datetime.now()
    timestamp_str = timestamp.strftime("%Y-%m-%dT%H-%M-%S")
    run_folder = os.path.join("outputs", f"run_{timestamp_str}")
    os.makedirs(run_folder, exist_ok=True)

    llm_logs = {
        "timestamp": timestamp.isoformat(),
        "url": url
    }

    return run_folder, llm_logs
