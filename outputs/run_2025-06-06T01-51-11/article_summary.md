```markdown
# Cosine Similarity

Cosine similarity measures the similarity between two non-zero vectors by calculating the cosine of the angle between them. It is used in machine learning and data analysis, especially in text analysis, document comparison, search queries, and recommendation systems.

*   Similarity measure calculates the distance between data objects based on their feature dimensions in a dataset.
*   A smaller distance indicates a higher similarity.

## Formula

The cosine similarity between two vectors is:

`S_C(x, y) = x . y / (||x|| * ||y||)`

Where:

*   `x . y` = dot product of vectors 'x' and 'y'
*   `||x||` and `||y||` = magnitudes (lengths) of vectors 'x' and 'y'

## Calculation Steps

1.  **Calculate the dot product:** Multiply corresponding components of the two vectors and sum the results.
2.  **Calculate the magnitude of each vector:**  Find the square root of the sum of the squares of each vector's components.
3.  **Calculate Cosine Similarity:** Divide the dot product by the product of the magnitudes.

## Example

Vectors:

*   x = {3, 2, 0, 5}
*   y = {1, 0, 0, 0}

1.  **Dot product:** `x . y = (3*1) + (2*0) + (0*0) + (5*0) = 3`
2.  **Magnitude of x:** `||x|| = √(3² + 2² + 0² + 5²) = √(9 + 4 + 0 + 25) = √38 ≈ 6.16`
3.  **Magnitude of y:** `||y|| = √(1² + 0² + 0² + 0²) = √1 = 1`
4.  **Cosine Similarity:** `S_C(x, y) = 3 / (6.16 * 1) ≈ 0.49`

## Dissimilarity

Dissimilarity can be calculated as:

`D_C(x, y) = 1 - S_C(x, y)`

In the example above:

`D_C(x, y) = 1 - 0.49 = 0.51`

## Angle Interpretation

*   θ = 0°: Vectors are highly similar (overlap).
*   θ = 90°: Vectors are dissimilar.
```