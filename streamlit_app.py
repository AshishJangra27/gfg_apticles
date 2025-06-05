import streamlit as st
import os
from datetime import datetime
from utils.scrape import scrape_article
from agents.agents import get_clean_summary_from_llm, get_webpage_design_from_llm, get_webpage_from_llm
from utils.support import llm_log, save_log, initialize_run

st.set_page_config(page_title="LLM Article → Webpage Generator", layout="wide")
st.title("🧠 LLM Article to Webpage Generator")

# Input
url = st.text_input("🔗 Enter article URL")

if st.button("🚀 Generate"):
    if not url.strip():
        st.warning("Please enter a valid URL.")
    else:
        run_folder, llm_logs = initialize_run(url)
        try:
            with st.spinner("🔍 Scraping article..."):
                raw_article = scrape_article(url, save=True, output_dir=run_folder)
            st.success("✅ Article scraped.")

            with st.spinner("✍️ Summarizing..."):
                summarised_article = get_clean_summary_from_llm(raw_article, save=True, output_dir=run_folder)
            llm_logs['summariser'] = llm_log(summarised_article)
            st.success("✅ Summary generated.")

            with st.spinner("🎨 Creating design brief..."):
                design_brief = get_webpage_design_from_llm(summarised_article['response'], save=True, output_dir=run_folder)
            llm_logs['designer'] = llm_log(design_brief)
            st.success("✅ Design brief ready.")

            with st.spinner("💻 Generating webpage code..."):
                webpage_code = get_webpage_from_llm(design_brief['response'], save=True, output_dir=run_folder)
            llm_logs['developer'] = llm_log(webpage_code)
            st.code(webpage_code['response'], language='html')

            # Save logs
            save_log(llm_logs, run_folder)
            st.success("📦 Token log saved.")

            with st.expander("📊 Token Usage"):
                st.json(llm_logs)

            st.info(f"📁 All files saved in: `{run_folder}`")

            st.subheader("⬇️ Download Files")

            def download_file_button(filename, label):
                file_path = os.path.join(run_folder, filename)
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as f:
                        st.download_button(label=label, data=f.read(), file_name=filename, mime="text/plain")

            download_file_button("webpage_code.html", "Download 💻 Webpage Code")

        except Exception as e:
            st.error(f"❌ Error: {e}")
