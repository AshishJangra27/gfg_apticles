# gfg_apticles -> Webpage Generator

This app lets you paste any article URL and converts it into:
- A clean summary
- A webpage design idea
- A working HTML code

Built with `Streamlit`, `Google Gemini`

## How to Use
1. Paste any article link
2. Click **Generate**
3. Get summary, design, and code — all auto-generated!


```
GFG_APPS/
├── agents/
│   ├── __init__.py
│   └── agents.py
│
├── outputs/
│   ├── run_2025-06-06T01-51-11/
│   │   ├── article_summary.md
│   │   ├── raw_article.md
│   │   ├── token_report.json
│   │   ├── webpage_code.html
│   │   └── webpage_design_prompt.md
│
├── utils/
│   ├── __init__.py
│   ├── prompts.py
│   ├── scrape.py
│   └── support.py
│
├── venv/                     # Python virtual environment
│
├── .env                      # 🔐 API keys (excluded via .gitignore)
├── .gitignore               # Git ignore rules
├── index.html               # Possibly preview or output viewer
├── main.py                  # Main orchestrator script
├── README.md                # Project documentation
├── requirements.txt         # Python dependency list
└── test.py                  # Script for testing functionality
```
