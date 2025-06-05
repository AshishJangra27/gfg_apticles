```markdown
## Cosine Similarity: Interactive Learning Experience

### 🧱 Section Breakdown & UI Layout

*   **Static Layout**: Single-page, fixed viewport.
    *   **Top**: Title Header ("Cosine Similarity Explorer") + Brief Introduction (max 2 sentences).
    *   **Left Panel**: Vector Input & Controls (Vector A, Vector B).
    *   **Center**: 2D Vector Visualization (interactive plot).
    *   **Right Panel**: Calculation Breakdown & Result Display.
    *   **Bottom**: Angle Interpretation & Key Considerations (toggleable).

*   **Essential Interactive Blocks**:
    *   Vector Input Fields (numerical input).
    *   2D Vector Plot (interactive).
    *   Calculation Breakdown (step-by-step).
    *   Angle Interpretation Visualizer.
    *   Key Considerations Toggle.

### 🕹️ Interactivity Mapping

1.  **Vector Input**:
    *   **Interaction**: Numerical input fields for Vector A (x1, y1) and Vector B (x2, y2).
    *   **Change**:
        *   Updates vector plot in the Center.
        *   Updates calculation breakdown in the Right Panel.
        *   Updates angle interpretation.
    *   **Type**: Numerical Input.

2.  **2D Vector Plot**:
    *   **Interaction**: Display of vectors A and B as arrows originating from the origin.
    *   **Change**:
        *   The angle between the vectors changes dynamically based on the input values.
        *   Visual highlighting of the angle.
    *   **Type**: Interactive plot.

3.  **Calculation Breakdown**:
    *   **Interaction**: Automatic calculation of the dot product, magnitudes, and cosine similarity.
    *   **Change**: Displays each step of the calculation (dot product, magnitude of A, magnitude of B, cosine similarity).
    *   **Type**: Dynamic Calculation Display.

4.  **Angle Interpretation Visualizer**:
    *   **Interaction**: Displays the cosine similarity value. A visual indicator (e.g., a gauge or a color scale) corresponds to the similarity value.
    *   **Change**: The visual indicator changes in real-time, reflecting the similarity value.
    *   **Type**: Visual Indicator.

5.  **Key Considerations Toggle**:
    *   **Interaction**: Button to toggle visibility of Key Considerations.
    *   **Change**: Shows/hides the section with key properties.
    *   **Type**: Toggle Button.

### 🧠 Learning Objective Behind Each Interaction

1.  **Vector Input**:
    *   **Intent**: Allow users to explore how different vector values affect the similarity score.
    *   **Outcome**: Understand the relationship between vector components and similarity.

2.  **2D Vector Plot**:
    *   **Intent**: Visualize vectors and their relationship. Reinforce that cosine similarity is about the angle.
    *   **Outcome**: Develop an intuitive understanding of vector similarity as angular proximity.

3.  **Calculation Breakdown**:
    *   **Intent**: Show the step-by-step calculation of cosine similarity.
    *   **Outcome**: Understand how the dot product and magnitudes contribute to the final score.

4.  **Angle Interpretation Visualizer**:
    *   **Intent**: Connect the cosine similarity score to a visual representation of the angle and similarity level.
    *   **Outcome**: Internalize the correlation between cosine similarity values and angular similarity.

5.  **Key Considerations Toggle**:
    *   **Intent**: Highlight crucial properties of cosine similarity.
    *   **Outcome**: Remember important characteristics like independence from magnitude, symmetry, and sensitivity to sparse data.

### 🧪 Cognitive Flow & Learner Progression

Left-to-Right Progression:

1.  **Vector Input**: User starts by defining the vectors (A and B).
2.  **2D Vector Plot**: Visualizes the vectors and the angle.
3.  **Calculation Breakdown**: User observes the calculation steps based on the input.
4.  **Angle Interpretation Visualizer**: See the similarity value reflected in the angle indicator.
5.  **Key Considerations Toggle**: User clicks to view further key considerations about the algorithm.

### ✨ Subtle Engagement Elements

*   **Hover Hints**: Tooltips on the vector plot highlighting vector names (A, B) upon hover.
*   **Animated Transitions**: Smooth transitions for vector updates on the plot.
*   **Guided tooltips:** On first load, a very brief, non-intrusive tooltip highlights the input areas and the plot.
```