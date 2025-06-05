```markdown
# Cosine Similarity Explained

Cosine similarity measures the similarity between two non-zero vectors by calculating the cosine of the angle between them. It's used in machine learning for tasks like text analysis and recommendation systems.

## Core Concept

Data objects are treated as vectors. Similarity is determined by the angle between the vectors, not their magnitude. A smaller angle indicates higher similarity.

## Formula

The cosine similarity between vectors *x* and *y* is calculated as:

```
S_C(x, y) = x . y / (||x|| * ||y||)
```

Where:

*   `x . y` = Dot product of vectors *x* and *y*.
*   `||x||` and `||y||` = Magnitudes (lengths) of vectors *x* and *y*.

## Calculation Example

Let:

*   x = {3, 2, 0, 5}
*   y = {1, 0, 0, 0}

Then:

1.  **Dot product:**
    `x . y = (3*1) + (2*0) + (0*0) + (5*0) = 3`
2.  **Magnitude of x:**
    `||x|| = √(3² + 2² + 0² + 5²) = √38 ≈ 6.16`
3.  **Magnitude of y:**
    `||y|| = √(1² + 0² + 0² + 0²) = √1 = 1`
4.  **Cosine Similarity:**
    `S_C(x, y) = 3 / (6.16 * 1) ≈ 0.49`

## Dissimilarity

Dissimilarity can be calculated as:

```
D_C(x, y) = 1 - S_C(x, y)
```

In the example above, the dissimilarity is: `1 - 0.49 = 0.51`

## Angle Interpretation

*   θ = 0°: Vectors are overlapping (highly similar).
*   θ = 90°: Vectors are dissimilar.

## Key Considerations

*   **Ignores Magnitude:** Considers only the angle, not the vector lengths.
*   **Symmetric:** Order of comparison doesn't matter.
*   **Sensitive to Sparse Data:** Can be ineffective for sparse vectors.
```