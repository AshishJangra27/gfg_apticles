import os

def generate_clean_summary_prompt(raw_article: str) -> str:
    """
    Generate a self-sufficient, focused summary of a technical article,
    filling in any missing information and limiting scope to at most 
    the core concepts needed for a single interactive learning app.
    """
    return f"""
You are a senior technical editor and interaction-focused content simplifier.

Your job is to **extract, infer, and restructure** only the **core conceptual content** from the raw article below so that it can directly drive an interactive learning webpage.  
If the raw input is incomplete or of low quality, you must **fill in missing details** (using your domain expertise) to make the summary self-sufficient.

---

**Raw Article Content**:
{raw_article}

---

**Requirements**:
- **Scope**: If the article covers more than 5 distinct concepts, select the top priority ones that together form a single coherent app experience.
- **Remove**: history, author opinions, case studies, intros/outros, ads, references, links, extraneous theory.
- **Retain & Infer**: essential concepts, mechanics, formulas, rules, algorithmic steps, and any code blocks needed for interactivity.
- **Structure**: Markdown with clear headings and bullets, under **500 words**, in simple, accurate language.

**Output**: Only the refined, self-contained conceptual content. No conclusions or commentary.
""".strip()


def generate_webpage_design_prompt(summarised_article: str) -> str:
    """
    Generate a design brief for a static, single-page interactive learning app,
    from the trimmed summary. Persona: instructional designer with 20+ years’ experience.
    """
    return f"""
You are an expert instructional designer with **20 years’ experience** in crafting interactive learning simulations and impeccable UI/UX.

Transform the following summarised content into a **static, no-scroll, single-page** design plan that emphasises **interactive graphics**, **real-time feedback**, and **exploration over text**.

---

📄 **Summarised Content**:
{summarised_article}

---

🎯 **Design Plan Must Include**:

1. **Section & Layout**  
   - List essential interactive components (e.g., simulators, visual explorers).  
   - Specify fixed positions: header, controls, main canvas—no scrolling.

2. **Interactivity Mapping**  
   - For each component:
     - User action (click, drag, slider).  
     - Visual change (diagram update, animation).  
     - Real-time feedback mechanism.

3. **Learning Objective**  
   - Purpose of each interaction and expected conceptual takeaway.

4. **Learner Flow**  
   - How users progress (e.g., sequential steps, toggle views).

5. **Engagement Enhancements**  
   - Subtle UX: hover hints, animated transitions, tooltips.

---

**Constraints**:  
- No quizzes or long text.  
- Keep format in clear Markdown lists and headings—no commentary.
""".strip()


def generate_webpage_prompt(design_brief: str) -> str:
    """
    Generate a strict prompt for a Veteran (20+ years) web developer
    to produce a flawless, static single-page HTML/CSS/JS app based 
    on the design brief.
    """
    return f"""
You are a minimalist web developer with **20+ years’ experience**. Build a **perfectly working**, static, non-scrollable single-page HTML app per the design below.

---

🧾 **Design Brief**:
{design_brief}

---

🧑‍💻 **Development Instructions**:

1. Single `.html` file with embedded CSS & JS only.
2. **GeeksforGeeks theme**:
   - Background: `#ffffff`, Primary: `#2f8d46`, Text: `#222222`.
3. **Static viewport**: no scroll; all UI and a central canvas must fit in one screen.
4. **Interactivity**: canvas-based graphics supporting click/drag/hover with real-time updates; optional external sliders.
5. **Quality**: every feature works flawlessly—no partial or buggy components.
6. **Footer**: fixed at bottom with links to your GitHub and LinkedIn:
   - `https://github.com/AshishJangra27/`
   - `https://www.linkedin.com/in/ashish-jangra/`
7. **No external libraries or imports**.

**Output**: Return only the complete `.html` code as plain text—no markdown or commentary nothing else.
""".strip()
