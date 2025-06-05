```markdown
## Binary Tree

A binary tree is a non-linear, hierarchical data structure where each node has at most two children: a left child and a right child.

*   **Root:** The topmost node.
*   **Leaves:** The bottom-most nodes.

### Node Representation

A node contains:

*   Data
*   Pointer to left child
*   Pointer to right child

### Terminologies

*   **Node:** Contains data and links to child nodes.
*   **Root:** Topmost node; no parent.
*   **Parent Node:** A node with children.
*   **Child Node:** Descendant of a parent node.
*   **Leaf Node:** A node with no children.
*   **Internal Node:** A node with at least one child.
*   **Depth of a Node:** Number of edges from the node to the root.
*   **Height of a Binary Tree:** Number of nodes from the deepest leaf to the root.

### Properties

*   Max nodes at level L: `2^L`
*   Max nodes in a tree of height H: `2^H – 1`
*   Leaf nodes = nodes with 2 children + 1
*   Min height of tree with N nodes: `Log2(N+1)`
*   Tree with L leaves has at least `|Log2L| + 1` levels

### Operations

1.  **Traversal:** Visiting all nodes.

    *   **Depth-First Search (DFS):** Explores as far down a branch as possible.
        *   **Preorder:** Node, Left, Right
        *   **Inorder:** Left, Node, Right
        *   **Postorder:** Left, Right, Node
    *   **Breadth-First Search (BFS):** Explores all nodes at the present depth level before moving to the next level.  Also known as Level Order Traversal.

2.  **Insertion:** Adding a new node.

    *   Create a root node if the tree is empty.
    *   Iteratively search for an empty left or right child at each level.
    *   Insert the new node in the first available position (starting with the left).

3.  **Searching:** Finding a node with a specific value.

    *   Use DFS or BFS to traverse the tree.
    *   If the node's data matches the search value, return true.
    *   If the tree is empty or the value isn't found after exploring all nodes, return false.

4.  **Deletion:** Removing a specific node.

    *   Find the node to be deleted.
    *   Replace the node's value with the value of the deepest rightmost node.
    *   Delete the deepest rightmost node.

### Complexity Analysis of Operations

| Operation             | Time Complexity | Auxiliary Space |
| --------------------- | --------------- | --------------- |
| In-Order Traversal    | O(n)            | O(n)            |
| Pre-Order Traversal   | O(n)            | O(n)            |
| Post-Order Traversal  | O(n)            | O(n)            |
| Insertion (Unbalanced) | O(n)            | O(n)            |
| Searching (Unbalanced) | O(n)            | O(n)            |
| Deletion (Unbalanced)  | O(n)            | O(n)            |
```