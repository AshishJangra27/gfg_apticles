import os

def generate_clean_summary_prompt(raw_article: str) -> str:
    return f"""
You are a senior technical editor with deep expertise in simplifying complex information.

Your task is to read the raw technical article below and produce a **summary of 1 to 3 lines** that clearly conveys the **core idea that can be turned into an interactive app**.

**Raw Article Content**:
{raw_article}

**Guidelines**:
- If the article covers multiple ideas, select only the **most impactful or teachable concept**.
- If content is unclear or missing, use your expertise to **infer the key message**.
- Keep the summary **simple, self-contained**, and ready for downstream design.

**Output Format**:
Return only the **1–3 line summary**, no extra formatting or commentary.
""".strip()




def generate_webpage_design_prompt(summarised_article: str) -> str:
    """
    Generate a design brief for a static, single-page interactive learning app,
    from the summarised concept. Persona: minimalist interaction designer with 20+ years’ experience.
    """
    return f"""
You are an interaction-first web educator and designer with **20+ years of experience** in minimalist educational app design.

Based on the summarised content below, design a **non-scrollable, single-page, static interactive HTML app** that communicates the concept clearly through user interaction.

---

📄 **Summarised Concept**:
{summarised_article}

---

🛠️ **Design Specifications**:

1. **File Structure**  
   - Single `.html` file.  
   - No external libraries or files.  
   - All layout and interactivity should be achievable with plain HTML/CSS/JS.

2. **Layout & Viewport**  
   - Must fully fit within a **static 1080p screen**.  
   - Fixed layout using `vh`/`vw`.  
   - Central **canvas or interaction panel** preferred.  
   - Header and footer clearly visible.

3. **Controls & Interactivity**  
   - Use interactivity **only if needed to teach the concept**.  
   - If helpful, recommend:
     - ✅ `Reset` and `Randomize` buttons
     - ✅ `Auto-Run` (demonstrates app by itself step-by-step)
     - ✅ `Next Step` (user manually moves through each step)
   - Provide inline visual feedback and **brief explanation text** (1–2 lines max)

4. **Visual Theme**  
   - Keep layout **minimal and clear**.  
   - Assume the developer will apply a **white background**, **black text**, and **subtle green accents** (`#2f8d46`) with the **GeeksforGeeks logo** in the top-left.

5. **Footer Content**  
   - Fixed at the bottom.  
   - Includes links to GitHub and LinkedIn.

---

📚 **Instructional Goals**:
- Let users **explore the idea**, not just read about it.
- All UI/UX must serve the learning process.
- Every interaction should support **conceptual clarity**.

---

**Non-Negotiables**:  
- No scrolling.  
- No unnecessary UI.  
- Everything shown must aid interaction and understanding.

Return the design brief in clear markdown-style formatting.
""".strip()



def generate_webpage_prompt(design_brief: str) -> str:
    """
    Generate a strict prompt for a veteran (20+ years) minimalist web developer
    to build a clean, branded, fully functional single-page HTML/CSS/JS app
    that includes GeeksforGeeks styling, green theme, interactive area,
    and two guided demo buttons: Auto-Run and Step-by-Step.
    """
    return f"""
You are a minimalist web developer with **20+ years of experience**. Build a **fully functional, static, single-screen HTML application** based on the design brief below, styled with green highlights and equipped with guided demonstration controls.

---

📐 **Design Brief**:
{design_brief}

---

🛠️ **Implementation Instructions**:

1. **File Structure**:
   - Use a single `.html` file.
   - All CSS and JavaScript must be embedded directly—no external files or libraries.

2. **Theme & Styling**:
   - Background: **white**
   - Text & borders: **black**
   - Accent Color: **GeeksforGeeks Green** `#2f8d46`
   - Font: **monospace**
   - Use **light gray** (`#cccccc`) for subtle UI elements

3. **Header**:
   - Top-left fixed
   - Must include:
     - GeeksforGeeks logo (`https://media.geeksforgeeks.org/gfg-gg-logo.svg`) — 32px height
     - A compact app title aligned with the logo

4. **Layout & Viewport**:
   - Fit completely within a **1080p screen** (non-scrollable)
   - Use `vh`/`vw` units
   - Required layout components:
     - Central `<canvas>` or interactive display area
     - Small **control panel** below or beside it
     - Inline feedback/explanation line (max 2 lines)

5. **Interactivity**:
   - Include at minimum:
     - ✅ `Reset` button
     - ✅ `Randomize` button
     - ✅ `Auto-Run` button: triggers **automated step-by-step demo**
     - ✅ `Next Step` button: lets user advance **manually one step at a time**
   - Only add more controls (e.g. sliders) **if the concept requires**
   - Ensure real-time updates and clarity of interaction
   - Inline explanation area updates during actions to show “what’s happening”

6. **Footer**:
   - Fixed at bottom
   - Must include:
     - GitHub: `https://github.com/AshishJangra27/`
     - LinkedIn: `https://www.linkedin.com/in/ashish-jangra/`
   - Styled in `#2f8d46`, clean and minimal hover effect

7. **Technical Constraints**:
   - No external JS/CSS/fonts/media (except the logo)
   - Use only **vanilla HTML, CSS, and JavaScript**

---

🧾 **Output Format**:
- Return **only the raw `.html` code as plain text**
- Do not include markdown formatting, comments, or explanations
""".strip()