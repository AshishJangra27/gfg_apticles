```markdown
# Cosine Similarity: Interactive Learning Experience

## 🧱 Section Breakdown & UI Layout

*   **Static Layout:** Single-page layout. Fixed viewport (no scrolling).

    *   **Header:** Title "Cosine Similarity".
    *   **Left Panel (30%):** Vector Input & Control Panel.
    *   **Right Panel (70%):** Visual Representation & Calculation Breakdown.
*   **Interactive Blocks:**

    1.  **Vector Input:** Numerical input fields for Vector x and Vector y.
    2.  **Visual Representation:** 2D Scatter Plot displaying vectors x and y. Updates in real-time as vector values change. Shows the angle between vectors.
    3.  **Calculation Breakdown:** Step-by-step calculation of dot product, magnitudes, and cosine similarity (dynamically updated).
    4.  **Dissimilarity Display:** A simple gauge or progress bar visualizing the dissimilarity score.
    5.  **Angle Interpretation:** A visual guide showing how the angle relates to similarity (0° = Similar, 90° = Dissimilar).

## 🕹️ Interactivity Mapping

1.  **Vector Input:**
    *   **Interaction:** Numerical input fields for x and y vector components (e.g., x1, x2, y1, y2, etc.). Plus/minus buttons to add/remove dimensions from the vectors. Limit to a reasonable number of dimensions for visualization (e.g. 2 or 3 dimensions max for the visualizer, but support more for calculation).
    *   **Change:** 2D Scatter Plot updates to reflect the new vector positions. The angle between the vectors updates. The calculation breakdown updates with the new values. The dissimilarity gauge changes.
    *   **Type:** Numerical input, buttons.

2.  **Visual Representation:**
    *   **Interaction:** Hovering over a vector highlights its components in the input fields and its contribution to the calculation breakdown. Clicking will "fix" focus so that the hover effect doesn't disappear.
    *   **Change:** Highlights corresponding input field & values in calculation breakdown.
    *   **Type:** Hover/Click events

3.  **Calculation Breakdown:**
    *   **Interaction:** None (primarily a display element). Hovering over a step will highlight the related parts in the Vectors.
    *   **Change:** Highlights corresponding vector components
    *   **Type:** Hover Events

4.  **Dissimilarity Display:**
    *   **Interaction:** None (directly reflects the Cosine Similarity calculation).
    *   **Change:** Updates the gauge or progress bar based on the calculated dissimilarity.
    *   **Type:** None

5.  **Angle Interpretation:**
    *   **Interaction:** Clickable angle ranges that explain "Highly Similar", "Somewhat Similar", "Dissimilar" to emphasize interpretation.
    *   **Change:** No direct change to the main visualization, but highlights and emphasizes the corresponding similarity level based on current angle.
    *   **Type:** Clickable Ranges

## 🧠 Learning Objective Behind Each Interaction

1.  **Vector Input:**
    *   **Intent:** To allow users to directly manipulate vector values and observe the impact on their visual representation and cosine similarity.
    *   **Outcome:** Understand how changing vector components affects the angle between vectors and, consequently, the similarity score.

2.  **Visual Representation:**
    *   **Intent:** To provide a visual intuition for vector similarity.
    *   **Outcome:** Learners can visually associate the angle between vectors with their similarity. Connect individual components to their visual contribution.

3.  **Calculation Breakdown:**
    *   **Intent:** To demystify the cosine similarity formula by showing each step in detail.
    *   **Outcome:** Understand how dot product and vector magnitudes contribute to the final similarity score.

4.  **Dissimilarity Display:**
    *   **Intent:** To provide a complementary view of the concept, focusing on how different the vectors are.
    *   **Outcome:** Reinforce the inverse relationship between similarity and dissimilarity.

5.  **Angle Interpretation:**
    *   **Intent:** To translate the numerical cosine similarity score into a qualitative understanding of similarity.
    *   **Outcome:** Learners can relate specific angle ranges to levels of similarity (e.g., 0-30 degrees = Highly Similar).

## 🧪 Cognitive Flow & Learner Progression

*   **Progression:** Left-to-right flow.
    1.  Start by entering values for Vector x and Vector y in the **Vector Input** panel.
    2.  Observe the corresponding changes in the **Visual Representation** (scatter plot) and the **Calculation Breakdown**.
    3.  See the impact on the **Dissimilarity Display**.
    4.  Refer to the **Angle Interpretation** to understand the qualitative similarity level.
*   The interaction is iterative. Users can continuously adjust vector values and observe the resulting changes across all elements.

## ✨ Subtle Engagement Elements

*   **Hover Hints:**
    *   When hovering over a vector in the scatter plot, highlight the corresponding values in the input fields.
    *   When hovering over a step in the Calculation Breakdown, highlight the corresponding vector components in the input fields and scatter plot.
*   **Animated Transitions:**
    *   Use smooth transitions for changes in the scatter plot and dissimilarity gauge.
*   **Guided Tooltips (Optional):**
    *   On first load, use a small, unobtrusive tooltip to guide the user to the Vector Input panel.
```