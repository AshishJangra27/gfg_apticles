```markdown
# Depth-First Search (DFS) for Graphs

**Last Updated:** March 29, 2025

Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It's analogous to traversing a tree by fully exploring the left subtree before moving to the right. A key consideration with graphs, unlike trees, is the presence of cycles, which can lead to infinite loops. Therefore, DFS uses a `visited` array to keep track of processed nodes and prevent revisiting them.

## Core Concepts

*   **Traversal Strategy:** Explores each branch as deeply as possible before backtracking.
*   **Visited Array:** A boolean array to mark visited nodes, preventing cycles and redundant processing.
*   **Recursive Implementation:**  DFS is commonly implemented using recursion, leveraging the call stack to maintain traversal state.
*   **Adjacency List/Matrix:** DFS operates on a graph represented either as an adjacency list (preferred for sparse graphs) or an adjacency matrix (suitable for dense graphs).

## Algorithm Steps (Single Source)

Given a graph represented by an adjacency list `adj` and a starting node `s`:

1.  **Mark the current node `s` as visited.**
2.  **Process the current node `s`.** (e.g., add it to the traversal result).
3.  **For each neighbor `i` of `s`:**
    *   **If `i` is not visited:**
        *   **Recursively call DFS on `i`.**

## Algorithm Steps (Complete Traversal - Disconnected Graph)

To traverse a potentially disconnected graph:

1.  **Initialize a `visited` array.**
2.  **For each vertex `i` in the graph:**
    *   **If `i` is not visited:**
        *   **Call the single-source DFS algorithm starting from `i`.**

## Example

Consider the following graph represented by the adjacency list `adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]` and a starting node of `0`.

1.  Start at node 0: Mark 0 as visited. Output: 0
2.  Move to node 1 (adjacent to 0): Mark 1 as visited. Output: 1
3.  Move to node 2 (adjacent to 1): Mark 2 as visited. Output: 2
4.  Move to node 3 (adjacent to 2): Mark 3 as visited. Output: 3 (backtrack to 2)
5.  Move to node 4 (adjacent to 2): Mark 4 as visited. Output: 4 (backtrack to 2, then backtrack to 1, then to 0)

Resulting DFS Traversal: `0 1 2 3 4`

## Code Examples (Illustrative)

**C++ (Single Source):**

```cpp
void dfsRec(vector<vector<int>> &adj, vector<bool> &visited, int s, vector<int> &res) {
    visited[s] = true;
    res.push_back(s);
    for (int i : adj[s])
        if (!visited[i])
            dfsRec(adj, visited, i, res);
}

vector<int> DFS(vector<vector<int>> &adj) {
    vector<bool> visited(adj.size(), false);
    vector<int> res;
    dfsRec(adj, visited, 0, res); //Start from source vertex 0
    return res;
}
```

## Time and Space Complexity

*   **Time Complexity:** O(V + E), where V is the number of vertices and E is the number of edges.  Each vertex and edge is visited at most once.
*   **Space Complexity:** O(V + E).  O(V) for the `visited` array and O(E) in worst case.  The recursive calls also contribute to the space complexity due to the call stack, which can be O(V) in the worst-case scenario (e.g., a skewed tree-like graph).

## Practical Applications

*   **Pathfinding:** Finding a path between two nodes.
*   **Cycle Detection:**  Determining if a graph contains cycles.
*   **Topological Sorting:** Ordering vertices in a directed acyclic graph (DAG).
*   **Connected Components:** Identifying sets of connected nodes in a graph.
*   **Maze Solving:**  Finding a path from start to end in a maze.

## Key Takeaways

DFS is a fundamental graph traversal algorithm. Understanding its recursive nature, the importance of the `visited` array, and its time/space complexity is crucial for solving various graph-related problems. The ability to adapt DFS for both single-source and complete graph traversals broadens its applicability.
```