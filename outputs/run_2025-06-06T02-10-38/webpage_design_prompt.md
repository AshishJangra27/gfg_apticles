```markdown
# Cosine Similarity: Interactive Learning Experience

## 🧱 Section Breakdown & UI Layout

*   **Header:** Title ("Cosine Similarity") and brief visual definition (angle between vectors).
*   **Main Area:** Split into two horizontal sections.
    *   **Top Section:** Interactive Cosine Similarity Visualizer (vectors and angle).
    *   **Bottom Section:** Calculation Step Visualizer (interactive breakdown of the formula).
*   **No Side Panels:** Focus on the core visualization and calculation.

## 🕹️ Interactivity Mapping

### 1. Interactive Cosine Similarity Visualizer (Top Section)

*   **User Interaction:**
    *   Draggable endpoints for two vectors (x and y) plotted on a 2D plane (limited to positive quadrant for simplicity).
*   **On-Screen Changes:**
    *   Vectors change length and direction in real-time.
    *   Angle between vectors is displayed numerically (degrees).
    *   Cosine similarity score is displayed numerically.
    *   Visual representation of the angle between vectors (highlighted sector).

### 2. Calculation Step Visualizer (Bottom Section)

*   **User Interaction:**
    *   Numerical input fields for components of vectors x and y (x1, x2, y1, y2 - all positive values).
    *   "Calculate" button.
*   **On-Screen Changes:**
    *   Displays each step of the Cosine Similarity calculation:
        *   Dot product (x . y)
        *   Magnitude of x (||x||)
        *   Magnitude of y (||y||)
        *   Cosine Similarity (S_C(x, y))
        *   Dissimilarity (D_C(x, y)) = 1 - S_C(x, y)
    *   The calculation steps are displayed sequentially with visual highlighting on each step as the user clicks 'Calculate'.

## 🧠 Learning Objective Behind Each Interaction

### 1. Interactive Cosine Similarity Visualizer

*   **Intent:** To visually demonstrate the relationship between the angle between two vectors and their cosine similarity score.
*   **Expected Learning Outcome:** Learners will understand that smaller angles (vectors pointing in similar directions) result in higher cosine similarity scores, and larger angles result in lower scores.

### 2. Calculation Step Visualizer

*   **Intent:** To break down the Cosine Similarity formula into its component parts and show how each part contributes to the final score.
*   **Expected Learning Outcome:** Learners will understand the role of dot product and magnitudes in determining cosine similarity. They'll grasp the mathematical process behind the visual representation.

## 🧪 Cognitive Flow & Learner Progression

1.  Start with the **Interactive Cosine Similarity Visualizer** (top section). This provides an intuitive visual understanding.
2.  Then, move to the **Calculation Step Visualizer** (bottom section) to understand the underlying mathematics.
3.  The layout encourages a top-down flow, from visual intuition to mathematical understanding.

## ✨ Subtle Engagement Elements

*   **Interactive Cosine Similarity Visualizer:**
    *   Hovering over a vector endpoint highlights the vector.
    *   Animated transition when dragging a vector.
*   **Calculation Step Visualizer:**
    *   Highlight the specific values from the vectors being used in each calculation step. For instance, when calculating the dot product, highlight the `x1` and `y1` values being multiplied in the vector component inputs above the equation.
    *   As each step is calculated, briefly highlight the corresponding field with the calculated result.
```