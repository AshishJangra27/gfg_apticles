import os

def generate_clean_summary_prompt(raw_article: str) -> str:
    """
    Generates a cleaned and structured version of a technical article focused strictly on 
    core concepts that can be turned into interactive visual learning components.
    """

    return f"""
            You are a senior technical editor and interaction-focused content simplifier.

            Your task is to **extract and restructure** only the **core conceptual content** from the raw article below, 
            so it can later be transformed into an interactive visual learning webpage.

            ---

            **Raw Article Content**:
            {raw_article}
            ---

            **Goal**:
            Remove everything that is not directly useful for building **visual, interactive learning components**.

            **Remove**:
            - History, author opinions, case studies, intros, outros
            - Repetitive content, ads, references, links
            - Unnecessary theory or background

            **Retain and Structure**:
            - Core **concepts**, **mechanics**, **formulas**, **rules**, and **step-by-step logic**
            - Clear explanations that can later be mapped to visuals or interactivity
            - Code blocks, flow diagrams (in text), algorithmic steps (if any)

            **Format**:
            - Use markdown with sections, bullet points, and clear headings
            - Keep it **under 500 words**
            - Maintain **technical accuracy**, but use clear, simple language

            **Expected Output**:
            Only the refined, structured conceptual content in markdown format.  
            Do **not** add summaries, conclusions, or commentary.
            """.strip()










def generate_webpage_design_prompt(summarised_article: str) -> str:
    """
    Generate a clean, focused prompt for designing a static, single-page interactive learning web app
    based strictly on core conceptual content.
    """
    return f"""
            ```You are an expert instructional designer and interaction-first web educator.

            Your goal is to **transform the following summarised technical content** into a **static, single-page, interactive learning experience** that allows users to explore the concept directly through visual and hands-on elements — not through text explanations.

            ---

            📄 **Summarised Concept**:
            {summarised_article}
            ---

            🎯 **Your Task**:
            Design a **visual learning experience** that enables learners to interact directly with the core concepts above.  
            The final output will be a **static, minimal HTML page** with a fixed viewport, designed for conceptual clarity and intuitive interaction.

            ---

            🧩 **Include the Following in Your Design Plan**:

            1. ### 🧱 Section Breakdown & UI Layout  
            - Identify all **essential interactive blocks or components** (e.g., concept simulator, visual explorer, step visualizer).
            - Describe **static layout**: What appears where on the screen (header, side panels, main area).
            - Follow a **viewport-first layout** (no long scrolling or paginated content).

            2. ### 🕹️ Interactivity Mapping  
            - For each concept, describe:
                - What will the user interact with?
                - What will change on screen (e.g., diagram, graph, formula)?
                - What type of interaction: sliders, buttons, click-points, code runners, flow diagrams?

            3. ### 🧠 Learning Objective Behind Each Interaction  
            - Explain the **intent** of each interaction: what concept does it clarify or demonstrate?
            - Mention expected learning outcome from that component.

            4. ### 🧪 Cognitive Flow & Learner Progression  
            - Suggest how the learner progresses across the page (e.g., left to right, progressive steps, toggle views).
            - Avoid navigation-heavy designs. Focus on **interaction-as-learning**.

            5. ### ✨ Subtle Engagement Elements  
            - Recommend any light, non-disruptive UX ideas like:
                - Hover-based hints, animated transitions for changes
                - Guided tooltips only if concept needs orientation

            ---

            📌 **Constraints**:
            - Do **not** include text-heavy sections, quizzes, or long explanations.
            - Keep all design strictly visual + interactive.
            - Output should be **structured in clear markdown**, no commentary.

            """.strip()



def generate_webpage_prompt(design_brief: str) -> str:
    """
    Generate a strict, theme-specific, and robust prompt for building a complete 
    static interactive webpage using HTML, CSS, and JavaScript — with GeeksforGeeks styling,
    canvas-based interaction, and perfectly working components.
    """

    return f"""
        You are a minimalist and highly disciplined web developer.

        Your task is to build a **fully functional, static, single-page HTML application** 
        based on the detailed design brief below. This page is built for learners to **directly interact with technical concepts**, with both visual clarity and flawless behavior.

        ---

        🧾 **Design Brief**:
        {design_brief}
        ---

        🧑‍💻 **Development Instructions**:

        1. Create a single `.html` file that includes:
        - Full **HTML structure**
        - Embedded **CSS**
        - Embedded or inline **JavaScript**

        2. Apply the **GeeksforGeeks color theme**:
        - Background: White (`#ffffff`)
        - Primary: GeeksforGeeks Green (`#2f8d46`)
        - Text: Dark (`#222222`)

        3. Use a **static, non-scrollable viewport layout**:
        - Fit all interface components within a single visible screen
        - Maintain clarity, whitespace, and focus on interactivity

        4. **Interactive Area Requirements**:
        - Include a central **canvas** or dynamic zone where users directly explore the concept
        - Support **in-canvas interactions** such as clicking, dragging, hovering, or manipulating elements directly
        - Allow optional external controls (sliders, toggles, selectors), but ensure all critical interactions are also canvas-driven

        5. ⚠️ **Functional Precision Requirement**:
        - Every feature or component you include must work **perfectly and without errors**
        - It’s acceptable to implement fewer features — but **nothing should be partially working or buggy**
        - Prioritize **technical accuracy, interaction feedback, and stability**

        6. UX/UI Expectations:
        - Clean layout, visually balanced
        - Smooth transitions if they help learning clarity
        - Font: system UI or monospace (optional), readable and accessible

        7. Add a **footer** with the following links:
        - GitHub: `https://github.com/AshishJangra27/`
        - LinkedIn: `https://www.linkedin.com/in/ashish-jangra/`
        - Footer should match the theme and stay fixed at the bottom if possible

        8. **Do not use**:
        - Any libraries, frameworks, CDNs, or media files
        - No external imports — use only raw HTML, CSS, and JS

        📦 **Output Format**:
        Return only the complete `.html` code as **plain text** — no markdown blocks, comments, or extra explanation.
        """.strip()
