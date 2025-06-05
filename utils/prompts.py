import os

def generate_clean_summary_prompt(raw_article: str) -> str:
    """
    Generate a prompt to clean, simplify, and structure a technical article.
    """

    return f"""
You are an expert technical editor and learning experience designer.

Below is a raw technical article scraped from a webpage:

---
{raw_article}
---

Please do the following:
1. Clean and simplify the content by removing repetitive or irrelevant text, links etc.
2. Summarize core concepts using clear, structured formatting (use steps, lists, formulas, etc).
3. Preserve technical accuracy but make it easier to understand for learners.
4. Generate a final 500 words summary of the article, focusing on key concepts and practical applications.

Return the refined article in markdown format.
""".strip()










def generate_webpage_design_prompt(summarised_article: str) -> str:
    """
    Generate a detailed prompt for designing an interactive single-page learning web application
    based on the summarised technical article.
    """
    return f"""
You are an expert educator, web designer, and interactive learning experience creator. 
You have created many successful interactive single-page web applications that help learners 
understand complex technical topics through visual and hands-on interactions.

Below is a summarised technical article intended for learning:

---
{summarised_article}
---

Your task is to create a complete **design plan** for an interactive single-page learning web application 
based on the above content. The goal is to help learners understand the core concepts by engaging 
with the content visually and interactively.

Please include:

1. **Key Components of the Webpage**  
   - Identify the major sections or blocks that should exist (e.g., interactive simulation, visual stepper, concept explorer).

2. **Design Plan as per the Topic**  
   - Suggest the most suitable structure and flow for this particular topic.  
   - Decide how the learner should navigate through or explore the concept.

3. **Visualization and Interactivity Plan**  
   - Identify which concepts must be visualized or interacted with.  
   - Describe how the interaction will work (e.g., sliders, buttons, graph nodes, draggable elements).  
   - Mention how changes in interaction will reflect on the screen.

4. **Exact UI/UX Layout of the Webpage**  
   - Describe the layout clearly (e.g., header, left panel: controls, right panel: animation area).  
   - Mention user experience ideas like animations, transitions, or responsiveness if needed.

5. **Educational Objective Behind Each Component**  
   - Explain how each visual/interactive element contributes to deeper understanding.  
   - Mention the expected learning outcome from each part.

6. **Suggestions for Enhancing Learner Engagement**  
   - Suggest any subtle elements that can keep learners engaged (e.g., progressive reveal, guided tooltips, mini walkthrough).

This webpage will have **only interactive learning** – no textual theory, quizzes, or practice questions. 
It should be a **single-page application** with strong technical depth and high educational value.

Return the output in clear, structured markdown format.
""".strip()










def generate_webpage_prompt(design_brief: str) -> str:
    """
    Generate a prompt for a minimalist developer to build a complete, single-page interactive webpage
    using only HTML, CSS, and JavaScript, based on the design instructions.
    """
    return f"""
You are a minimalist and highly skilled web developer who follows the "information over decoration (IO)" philosophy. 
You build beautiful, functional, and focused single-page web applications using only HTML, CSS, and JavaScript.

Below is a design brief from a designer describing the exact plan for a single-page interactive learning webpage:

---
{design_brief}
---

Your task is to:

1. Create one single HTML file that includes everything — HTML structure, CSS styles, and JavaScript functionality.
2. Focus heavily on the interactive portion as described. Give it maximum screen space.
3. Use only monospace font throughout the page.
4. The title should be centered at the top of the page.
5. Add a footer at the bottom with the GitHub link: `https://github.com/ashishmentor`.
6. Ensure the entire page is clean, minimal, and responsive.
7. The result must be working and include all interactivity as described.

Return only the **complete single HTML file code in raw text format not code block**, no extra explanations or commentary. Just the code.
""".strip()