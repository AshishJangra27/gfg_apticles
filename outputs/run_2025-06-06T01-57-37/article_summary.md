```markdown
# Cosine Similarity

Cosine similarity measures the similarity between two non-zero vectors by calculating the cosine of the angle between them.

*   Used in machine learning, data analysis, text analysis, document comparison, search queries, and recommendation systems.

## Concept

Data objects are treated as vectors. Smaller distance between vectors indicates higher similarity.

## Formula

```
S_C(x, y) = x . y / (||x|| * ||y||)
```

Where:

*   `x . y` = dot product of vectors x and y
*   `||x||` and `||y||` = magnitude (length) of vectors x and y

## Calculation Example

Vectors:

*   x = {3, 2, 0, 5}
*   y = {1, 0, 0, 0}

1.  **Dot Product:**

    `x . y = (3 * 1) + (2 * 0) + (0 * 0) + (5 * 0) = 3`
2.  **Magnitude of x:**

    `||x|| = √(3² + 2² + 0² + 5²) = √38 ≈ 6.16`
3.  **Magnitude of y:**

    `||y|| = √(1² + 0² + 0² + 0²) = √1 = 1`
4.  **Cosine Similarity:**

    `S_C(x, y) = 3 / (6.16 * 1) ≈ 0.49`

## Dissimilarity

`D_C(x, y) = 1 - S_C(x, y)`

In the example above:

`D_C(x, y) = 1 - 0.49 = 0.51`

## Angle Interpretation

*   θ = 0°: Vectors overlap (similar).
*   θ = 90°: Vectors are dissimilar.
```