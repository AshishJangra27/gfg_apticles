```markdown
# SQL INNER JOIN: Interactive Learning Experience

## 🧱 Section Breakdown & UI Layout

*   **Layout**: Fixed viewport, three main horizontal sections:
    *   **Header (Top)**: Title & brief concept introduction (visual).
    *   **Interactive Area (Middle)**: Table explorer, SQL Runner, and visual representation of the join.
    *   **Comparison (Bottom)**: INNER JOIN vs. OUTER JOIN visual comparison.
*   **Essential Interactive Blocks**:
    *   Table Explorer: Interactive table viewer.
    *   SQL Runner: Simplified SQL editor and output display.
    *   Join Visualizer: Diagram showing data flow and matched rows.
    *   Comparison Toggle: Switches between INNER and OUTER JOIN visualization.

## 🕹️ Interactivity Mapping

1.  **Table Explorer**:
    *   Interaction: Clickable table headers to highlight columns.
    *   Change: Highlights selected column across both professor and teacher tables.
    *   Interaction: Row selection (click).
    *   Change: Highlights the selected row and any related row based on `prof_id` in the other table, preparing data for the SQL Runner.
2.  **SQL Runner**:
    *   Interaction: Pre-filled SQL query (editable with dropdowns for table & column selection). Run button.
    *   Change: Executes simplified query internally (JS).  Displays resulting table below. Updates the Join Visualizer.
    *   Interaction: Hover over column names in the resulting table.
    *   Change: Highlights corresponding columns in the Table Explorer.
3.  **Join Visualizer**:
    *   Interaction: None (passive visual representation updated by SQL Runner).
    *   Change: Venn diagram or similar visualization that visually represents how the tables overlap and the INNER JOIN selects the intersecting data. Displays matching rows prominently.
4.  **Comparison Toggle**:
    *   Interaction: Toggle switch (INNER/OUTER).
    *   Change: Updates Join Visualizer to show OUTER JOIN (LEFT, RIGHT, or FULL selectable via radio buttons). Highlights unmatched rows differently (e.g., grayed out).

## 🧠 Learning Objective Behind Each Interaction

1.  **Table Explorer**:
    *   Intent: Visually understand table structure and relationships between `professor` and `teacher` tables.
    *   Outcome: Learners should be able to identify the common column (`prof_id`/`ID`) used for joining.
2.  **SQL Runner**:
    *   Intent: Experiment with the SQL query to understand how it filters and combines data.
    *   Outcome: Learners should understand how changing the query affects the output.
3.  **Join Visualizer**:
    *   Intent: Abstract representation of the join operation, reinforcing the concept of matching rows.
    *   Outcome: Learners should internalize how INNER JOIN selects only the intersection of the data.
4.  **Comparison Toggle**:
    *   Intent: Contrast INNER JOIN with OUTER JOIN to solidify understanding of what INNER JOIN *excludes*.
    *   Outcome: Learners should understand the difference between INNER and OUTER joins and when to use each.

## 🧪 Cognitive Flow & Learner Progression

1.  Start with **Table Explorer** to understand the raw data.
2.  Move to **SQL Runner** to see the query and its output (initially pre-filled).
3.  Observe the **Join Visualizer** to connect the SQL query with the visual representation of the join.
4.  Use the **Comparison Toggle** to explore how OUTER JOIN differs from INNER JOIN.

## ✨ Subtle Engagement Elements

*   Hover over table cells in Table Explorer to briefly highlight the corresponding data in the SQL Runner output (if applicable).
*   Animated transition in Join Visualizer when the SQL Runner output changes.
*   Subtle pulse animation on matching rows in both tables when a row is selected in either table.
*   Tooltips on comparison toggle explaining the different OUTER JOIN types (LEFT, RIGHT, FULL) when hovered over.
```