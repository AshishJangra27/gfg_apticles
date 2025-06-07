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
    to produce a clean, interactive, single-page HTML/CSS/JS app based on the design brief,
    allowing randomization, real-time interaction, and lightweight visual explanations.
    """
    return f"""
You are a minimalist web developer with **20+ years of experience**. Build a **fully functional, static, single-screen HTML application** based on the design brief below, giving users **freedom to interact, explore, and learn visually**.

---

📐 **Design Brief**:
{design_brief}

---

🛠️ **Implementation Instructions**:

1. **File Structure**:
   - Use a single `.html` file.
   - Embed all **HTML**, **CSS**, and **JavaScript** in the same file.
   - No external libraries, stylesheets, or media files.

2. **Theme & Styling**:
   - Background: **white**
   - Primary text and UI elements: **black**
   - Secondary elements (hints, borders, indicators): **light gray** `#888888` or `#cccccc`
   - Font: **monospace**, clean, readable
   - Use **contrast-aware layout** — ensure all content is clearly visible under daylight and dark mode environments.

3. **Layout & Viewport**:
   - Design must fit entirely within a **1080p screen** (no scrolling).
   - Use `vh` and `vw` units for responsiveness.
   - Layout must include a **central interactive area** (like a `<canvas>`, control panel, or graph).
   - Optional sections for:
     - **Live explanation text** (1–2 lines max, inline, dynamically updated)
     - **Action buttons** (e.g., Randomize, Reset, Demo Mode)

4. **Interactivity**:
   - Allow users to **interact with the concept in real-time** (if applicable).
   - Populate the app with **new random data** or variables on each refresh or via a button.
   - If applicable, support:
     - **Click**, **drag**, **hover**, or **slider-based input**
     - Instant updates to visuals and brief explanations
   - Add:
     - A **Randomize** button
     - A **Reset** button
     - An optional **Auto-demo** toggle
   - Use **hover hints** or **inline explanation text** to describe what's happening in the interaction (keep it short and simple).

5. **Functionality Requirements**:
   - All features must be **bug-free**, **fully implemented**, and **intuitively usable**
   - Every interaction must make the **learning objective clearer**
   - Avoid decorative or overly complex behavior — **simplicity + clarity** is key

6. **Footer**:
   - Fixed at the bottom
   - Includes:
     - GitHub: `https://github.com/AshishJangra27/`
     - LinkedIn: `https://www.linkedin.com/in/ashish-jangra/`
   - Style matches the theme (black/gray text on white)

7. **Technical Constraints**:
   - No external libraries, fonts, icons, or media
   - Use only **vanilla HTML, CSS, and JavaScript**

---

🧾 **Output Format**:
- Return only the full `.html` code as **plain text**
- Do not return markdown, comments, or explanation — just the raw HTML
""".strip()
