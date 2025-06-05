```markdown
# Binary Tree Concepts

A Binary Tree is a non-linear, hierarchical data structure where each node has at most two children: a left child and a right child.
*   The topmost node is the **root**.
*   The bottom-most nodes are **leaves**.

## Representation

Each node contains:
*   Data
*   Pointer to the left child
*   Pointer to the right child

## Terminologies

*   **Node:** Contains data and links to child nodes.
*   **Root:** Topmost node; no parent.
*   **Parent Node:** A node with child nodes.
*   **Child Node:** Descendant of another node (its parent).
*   **Leaf Node:** A node with no children.
*   **Internal Node:** A node with at least one child.
*   **Depth of a Node:** Number of edges from node to the root (root's depth is 0).
*   **Height of a Binary Tree:** Number of nodes from the deepest leaf node to the root node.

## Properties

*   Max nodes at level L: 2<sup>L</sup>
*   Max nodes in a tree of height H: 2<sup>H</sup> – 1
*   Number of leaf nodes = Number of nodes with 2 children + 1
*   Min height of tree with N nodes: Log<sub>2</sub>(N+1)
*   A Binary Tree with L leaves has at least | Log2L |+ 1 levels

## Types

*   **On the basis of Number of Children**
    *   Full Binary Tree
    *   Degenerate Binary Tree
    *   Skewed Binary Trees
*   **On the basis of Completion of Levels**
    *   Complete Binary Tree
    *   Perfect Binary Tree
    *   Balanced Binary Tree
*   **On the basis of Node Values:**
    *   Binary Search Tree
    *   AVL Tree
    *   Red Black Tree
    *   B Tree
    *   B+ Tree
    *   Segment Tree

## Operations

### 1. Traversal

Visiting all nodes in a specific order.

*   **Depth-First Search (DFS):**
    *   **Preorder:** Node, Left, Right
    *   **Inorder:** Left, Node, Right
    *   **Postorder:** Left, Right, Node
*   **Breadth-First Search (BFS):**
    *   **Level Order:** Visit nodes level by level, from left to right.

### 2. Insertion

Adding a new node.
1.  If the tree is empty, create the root node.
2.  Otherwise, use level order traversal to find the first available (empty) left or right child position.
3.  Insert the new node at that position (start with left child, by convention)

### 3. Searching

Finding a node with a specific value.

*   Use DFS or BFS to traverse the tree.
*   Compare the value of each node with the target value.
*   If found, return `true`; otherwise, return `false`.

### 4. Deletion

Deleting a node while preserving the tree structure.
1.  Find the node to delete (target node) using traversal.
2.  Find the deepest rightmost node in the tree.
3.  Replace the target node's value with the deepest rightmost node's value.
4.  Delete the deepest rightmost node.

## Complexity Analysis of Binary Tree Operations

| Operation             | Time Complexity | Auxiliary Space |
|----------------------|-----------------|-----------------|
| In-Order Traversal    | O(n)            | O(n)            |
| Pre-Order Traversal   | O(n)            | O(n)            |
| Post-Order Traversal  | O(n)            | O(n)            |
| Insertion (Unbalanced) | O(n)            | O(n)            |
| Searching (Unbalanced) | O(n)            | O(n)            |
| Deletion (Unbalanced)  | O(n)            | O(n)            |