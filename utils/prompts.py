import os

def generate_clean_summary_prompt(raw_article: str) -> str:
    
    return f"""
You are a senior technical editor with deep expertise in simplifying complex information.

Your task is to read the raw technical article below and produce a **single-line summary** that captures the **central idea or insight** of the content.

**Raw Article Content**:
{raw_article}

**Guidelines**:
- If the article contains multiple ideas, focus on the **most important, overarching concept**.
- If information is missing or unclear, **infer the core message** using your domain expertise.
- Use **clear, concise, and self-contained language**.
- No bullet points, formatting, or commentary—just **one sentence** that stands on its own.

**Output Format**:
Return only the **one-sentence summary**.
""".strip()




def generate_webpage_design_prompt(summarised_article: str) -> str:
    """
    Generate a design brief for a static, single-page interactive learning app,
    from the trimmed summary. Persona: minimalist web developer with 20+ years’ experience.
    """
    return f"""
You are a minimalist web developer with **20+ years of experience**. Build a **basic, static, non-scrollable, single-page interactive visual learning HTML app** based on the summarised content below.

---

📄 **Summarised Content**:
{summarised_article}

---

🛠️ **Design Specifications**:

1. **File Structure**  
   - Single `.html` file only.  
   - Inline CSS and JavaScript.  
   - No external libraries or files.

2. **Layout & Viewport**  
   - Entire app must fit within a **single static viewport** (no scrolling).  
   - Fixed layout using `vh`/`vw` units.  
   - A central **canvas** or key interactive area is preferred (if applicable).  
   - Header and footer must be clearly positioned and visible.

3. **Visual Theme**  
   - Background: **white**.  
   - Text & elements: **black**, clean.  
   - Font: **monospace**, readable, no styling distractions.

4. **Interactivity**  
   - Only add interactivity **if the concept naturally requires it** for learning.  
   - You may skip advanced interactions if they don’t aid the learning experience.  
   - Use your expertise to decide how best to **convey the main idea interactively**.  
   - If added:
     - Support **click**, **drag**, or **hover**
     - Add a **reset** button or **demo toggle** (optional)
     - Light hover hints allowed

5. **Footer Section**  
   - Fixed at the bottom of the screen.  
   - Includes:
     - [GitHub](https://github.com/AshishJangra27/)  
     - [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)  
   - Styled to match the clean theme.

---

📚 **Instructional Priorities**:
- Convey the **core concept visually and interactively** (if needed).  
- Avoid unnecessary UI or complexity.  
- Keep the design clean, direct, and intuitive.

---

**Non-Negotiables**:  
- No scrolling.  
- No unnecessary features.  
- Everything included must clearly support understanding of the main idea.

Return design brief
""".strip()



def generate_webpage_prompt(design_brief: str) -> str:
    """
    Generate a strict prompt for a veteran (20+ years) minimalist web developer
    to produce a clean, static, single-page HTML/CSS/JS app based on the design brief,
    using a white background, black text, and monospace font.
    """
    return f"""
You are a minimalist web developer with **20+ years of experience**. Build a **fully functional, static, single-screen HTML application** strictly based on the following design brief.

---

📐 **Design Brief**:
{design_brief}

---

🛠️ **Implementation Instructions**:

1. **File Structure**:
   - Use a single `.html` file.
   - All CSS and JavaScript must be embedded in the same file (no external stylesheets or scripts).

2. **Theme & Styling**:
   - Background: **white**
   - Text and elements: **black**
   - Font: **monospace**, clean and readable
   - Avoid unnecessary styling, colors, or visual effects

3. **Layout & Viewport**:
   - The entire app must fit within a **1080p screen** without scrolling
   - Use CSS `vh` and `vw` units to maintain a static layout
   - If interactivity is required, use a central `<canvas>` or clearly defined interaction area

4. **Interactivity**:
   - Add interactivity **only if it directly serves the concept** being taught
   - If used, support:
     - **Click**, **drag**, or **hover**
     - **Basic feedback** (no animations or transitions)
   - A simple **reset** button or **auto-demo** toggle may be included if helpful

5. **Functionality Requirements**:
   - All components must be **fully working and bug-free**
   - Keep user interactions intuitive and lightweight
   - Do not add complexity unless essential for understanding the concept

6. **Footer**:
   - Fixed at the bottom of the viewport
   - Includes:
     - GitHub: `https://github.com/AshishJangra27/`
     - LinkedIn: `https://www.linkedin.com/in/ashish-jangra/`
   - Styled simply to match the rest of the theme (black text on white background)

7. **Technical Constraints**:
   - Do not use any external libraries, frameworks, fonts, or media
   - Use only **vanilla HTML, CSS, and JavaScript**

---

🧾 **Output Format**:
- Return **only the complete `.html` code as plain text**
- No markdown, no explanations, no comments — just the HTML
""".strip()
