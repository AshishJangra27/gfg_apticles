```markdown
# Cosine Similarity

Cosine similarity measures the similarity between two non-zero vectors by calculating the cosine of the angle between them. It is used in machine learning and data analysis for tasks like text analysis and recommendation systems.

*   Similarity is inversely proportional to distance between data objects.

Cosine similarity treats data objects as vectors.

## Formula

The cosine similarity between two vectors x and y is calculated as:

`S_C(x, y) = x . y / (||x|| * ||y||)`

Where:

*   `x . y` is the dot product of vectors x and y.
*   `||x||` and `||y||` are the magnitudes (lengths) of vectors x and y.

## Calculation Example

Let's say:

*   `x = {3, 2, 0, 5}`
*   `y = {1, 0, 0, 0}`

Then:

1.  **Dot Product:** `x . y = (3*1) + (2*0) + (0*0) + (5*0) = 3`
2.  **Magnitude of x:** `||x|| = √(3² + 2² + 0² + 5²) = √38 ≈ 6.16`
3.  **Magnitude of y:** `||y|| = √(1² + 0² + 0² + 0²) = √1 = 1`
4.  **Cosine Similarity:** `S_C(x, y) = 3 / (6.16 * 1) ≈ 0.49`

## Dissimilarity

Dissimilarity can be calculated as:

`D_C(x, y) = 1 - S_C(x, y)`

In the example above:

`D_C(x, y) = 1 - 0.49 = 0.51`

## Angle Interpretation

*   θ = 0°: Vectors are similar (overlap).
*   θ = 90°: Vectors are dissimilar.

## Considerations

*   **Sparse Data:** Can be ineffective if there are many zero values.
*   **Magnitude Ignored:** Only considers the angle, not the magnitude of the vectors.
*   **Symmetric:** Does not account for the order of comparison.
```