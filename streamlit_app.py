import streamlit as st
import os
from datetime import datetime
import streamlit.components.v1 as components

from utils.scrape import scrape_article
from agents.agents import get_clean_summary_from_llm, get_webpage_design_from_llm, get_webpage_from_llm
from utils.support import llm_log, save_log, initialize_run

st.set_page_config(page_title="GFG Apticles: LLM Article → Webpage Generator", layout="wide")

# HEADER
st.title("🧠 GFG Apticles: LLM Article to Webpage Generator")
st.caption("📎 Paste an article URL below to generate a fully interactive webpage!")

# INPUT
url = st.text_input("🔗 Enter Article URL")

if st.button("🚀 Generate"):
    if not url.strip():
        st.warning("⚠️ Please enter a valid URL.")
    else:
        run_folder, llm_logs = initialize_run(url)
        progress = st.progress(0, text="Initializing...")

        try:
            with st.spinner("🔍 Scraping article..."):
                raw_article = scrape_article(url, save=True, output_dir=run_folder)
            progress.progress(25, text="✅ Scraped article.")
            st.success("✅ Article scraped successfully.")

            with st.spinner("✍️ Summarizing content..."):
                summarised_article = get_clean_summary_from_llm(raw_article, save=True, output_dir=run_folder)
            llm_logs['summariser'] = llm_log(summarised_article)
            progress.progress(50, text="✅ Summary generated.")
            st.success("✅ Summary complete.")

            with st.spinner("🎨 Creating design brief..."):
                design_brief = get_webpage_design_from_llm(summarised_article['response'], save=True, output_dir=run_folder)
            llm_logs['designer'] = llm_log(design_brief)
            progress.progress(75, text="✅ Design brief ready.")
            st.success("✅ Design prepared.")

            with st.spinner("💻 Generating webpage code..."):
                webpage_code = get_webpage_from_llm(design_brief['response'], save=True, output_dir=run_folder)
            llm_logs['developer'] = llm_log(webpage_code)
            progress.progress(100, text="✅ Webpage generated.")
            st.success("✅ Webpage code generated.")

            # Save token logs
            save_log(llm_logs, run_folder)

            # Render full-screen output
            st.subheader("🌐 Final Rendered Webpage")
            components.html(webpage_code['response'], height=900, scrolling=True)

            # Download Section
            st.subheader("⬇️ Download Files")

            def download_file_button(filename, label):
                file_path = os.path.join(run_folder, filename)
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as f:
                        st.download_button(label=label, data=f.read(), file_name=filename, mime="text/plain")

            download_file_button("webpage_code.html", "💻 Download Webpage Code")

            with st.expander("📊 Token Usage"):
                st.json(llm_logs)

            st.info(f"📁 All files saved in: `{run_folder}`")

        except Exception as e:
            st.error(f"❌ Error: {e}")