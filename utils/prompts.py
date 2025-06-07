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
You are a minimalist web developer with **20+ years of experience**. Build a **perfectly working, static, non-scrollable, single-page interactive visual learning HTML app** based on the summarised content below.

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
   - Central interactive **canvas element** is required.  
   - Header, controls, and footer must be clearly positioned and visible.

3. **Visual Theme**  
   - Background: **black**.  
   - UI highlights: **neon colors** (blue, green, pink, etc.) with glow effects.  
   - Clean, high-contrast, futuristic aesthetic.

4. **Interactivity**  
   - Canvas must support:  
     - **Click**, **drag**, **hover** actions.  
     - Real-time visual updates.  
   - Add buttons for **reset**, **randomize**, and **auto-demo mode**.  
   - Use **tooltips**, **animated transitions**, and **custom cursors** to enhance usability.

5. **Functionality Extensions**  
   - Add **toggle controls** to activate/deactivate layers or elements.  
   - Include an **FPS display** or activity indicator.  
   - Auto-play demo runs through the concept without user input.

6. **Footer Section**  
   - Fixed at the bottom of the screen.  
   - Includes:  
     - [GitHub](https://github.com/AshishJangra27/)  
     - [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)  
   - Styled to match the neon theme.

---

📚 **Instructional Priorities**:
- Emphasize **visual learning over text**.  
- Each interaction must convey a **clear conceptual takeaway**.  
- Flow should feel **natural, exploratory, and intuitive**.

---

**Non-Negotiables**:  
- No scrolling.  
- No incomplete or buggy features.  
- No long text explanations or quizzes.  
- All UI elements must function flawlessly.

Return design brief
""".strip()



def generate_webpage_prompt(design_brief: str) -> str:
    """
    Generate a strict prompt for a veteran (20+ years) minimalist web developer
    to produce a flawless, static, single-page HTML/CSS/JS app based on the given design brief,
    using a dark theme with neon accents.
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
   - All CSS and JavaScript must be embedded within the same file (no external stylesheets or scripts).

2. **Theme & Styling**:
   - Use a **dark neon theme**:
     - Background: `#000000` (pure black)
     - Primary accents: **neon colors** like `#39ff14` (green), `#00ffff` (cyan), `#ff00ff` (magenta)
     - Text: light shades like `#f0f0f0`
   - Apply **glow effects** on interactive elements.
   - Maintain pixel-perfect alignment and clean UI spacing.

3. **Layout & Viewport**:
   - The app must be **non-scrollable** and fit entirely within a **1080p screen**.
   - Use CSS `vh` and `vw` units to make layout responsive to screen size.
   - A central `<canvas>` element must handle all graphical interactivity.

4. **Interactivity**:
   - The canvas must support:
     - **Click**, **drag**, and **hover** events.
     - **Real-time visual updates**.
   - Include:
     - **Reset**, **Randomize**, and **Auto-demo** buttons.
     - Optional sliders or toggles if required.
     - Tooltips and animated transitions.
     - Custom cursors for interaction cues (pointer, grab, crosshair, etc.).

5. **Functionality Requirements**:
   - All components must be **flawlessly implemented**.
   - No partial or placeholder functionality.
   - Ensure responsive, smooth, and intuitive user experience.

6. **Footer**:
   - Fixed at the bottom of the viewport.
   - Includes:
     - GitHub: `https://github.com/AshishJangra27/`
     - LinkedIn: `https://www.linkedin.com/in/ashish-jangra/`
   - Styled with neon text and links; must not interfere with main UI or canvas.

7. **Technical Constraints**:
   - **No external libraries, fonts, or frameworks**.
   - Use **vanilla HTML, CSS, and JS only**.

---

🧾 **Output Format**:
- Return **only the complete `.html` code as plain text**.
- **No markdown**, no explanations, no comments—just the full HTML content.
""".strip()
