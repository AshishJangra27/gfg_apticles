```markdown
## Binary Tree Interactive Learning Experience: Design Plan

### 🧱 Section Breakdown & UI Layout

*   **Static Layout:** Single-page, fixed viewport (no scrolling).
    *   **Header:** Title "Binary Tree Explorer" (top-center)
    *   **Left Panel:** Interactive Tree Builder & Visualizer (30% width). Users construct and visualize trees.
    *   **Right Panel:** Interactive Operations & Properties Explorer (70% width). Demonstrates traversals, insertion, deletion, and properties.

*   **Interactive Blocks/Components:**
    1.  **Tree Builder/Visualizer (Left Panel):** Allows users to add/remove nodes to construct a custom binary tree.
    2.  **Traversal Visualizer (Right Panel):** Demonstrates Preorder, Inorder, Postorder, and Level Order traversals on the tree built in the Left Panel.
    3.  **Insertion Visualizer (Right Panel):** Animates the process of inserting a new node.
    4.  **Deletion Visualizer (Right Panel):** Animates the process of deleting a node.
    5.  **Properties Display (Right Panel):** Dynamically displays tree properties (height, number of nodes, etc.) based on the tree built in the Left Panel.
    6.  **Type Explorer (Right Panel):** Toggle display for Full, Complete, Perfect, Balanced, Degenerate and Skewed trees.

### 🕹️ Interactivity Mapping

| Concept            | Interaction                               | Screen Change                                                                                                                                                                                                                  | Interaction Type        |
| ------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Tree Construction  | Add Node Button (with input value), Delete Node (click on node) | Left Panel Tree Diagram updates in real-time to reflect added/deleted nodes. The node labels reflect the data input.                                                                                                  | Buttons, Click Points    |
| Traversal          | Select Traversal Type (Preorder, Inorder, Postorder, Level Order), "Start" Button | Right Panel: The nodes in the tree built in the Left Panel are highlighted in the selected traversal order, with a short delay between highlights. A text box displays the traversal output.                                           | Dropdown, Button          |
| Insertion          | Input value for new node, "Insert" Button | Right Panel: Animates the process of finding the first available spot (level order traversal) and inserting the new node.  The tree in the Right Panel mirrors the left panel in real time, and new insertion happens in right panel. | Input Field, Button     |
| Deletion           | Click on node to delete, "Delete" Button   | Right Panel: Animates the process of finding the deepest rightmost node, replacing the target node's value, and deleting the rightmost node. The tree in the Right Panel mirrors the left panel in real time, and deletion happens in right panel.                                               | Click Points, Button    |
| Tree Properties    | Tree built in Left Panel                   | Right Panel: Displays dynamically updated values for Height, Number of Nodes, Number of Leaf Nodes. Formulas can be visible on hover.                                                                                        | Automatic Update       |
| Tree Types       | Click on the different types of binary trees.                  | Right Panel: Displays a static example graph of the specific tree.                                                                                         | Click Points       |

### 🧠 Learning Objective Behind Each Interaction

| Interaction                      | Learning Objective                                                                                               | Expected Outcome                                                                                                                                                                                   |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tree Construction                | Understand the fundamental structure of a binary tree and how nodes are connected.                             | Learners can build arbitrary binary trees and visualize their structure.                                                                                                                       |
| Traversal                        | Learn and visualize different tree traversal algorithms (DFS, BFS).                                             | Learners can identify the order in which nodes are visited for each traversal method.                                                                                                      |
| Insertion                        | Understand the process of inserting a new node into a binary tree using level order traversal.                  | Learners can visualize how a new node is placed in a binary tree to maintain its structure.                                                                                                    |
| Deletion                         | Understand the process of deleting a node from a binary tree and maintaining its structure.                     | Learners can visualize the node replacement and deletion process.                                                                                                                             |
| Tree Properties                  | Understand how tree properties (height, number of nodes) relate to the tree's structure.                       | Learners can observe how changes to the tree structure affect its properties.                                                                                                              |
| Tree Types      | Understand the visual aspects that make each type of tree special.                     | Learners can look at the visual example graph of a full, skewed, perfect, etc. tree.                                                                                                                             |

### 🧪 Cognitive Flow & Learner Progression

1.  **Start with Tree Construction (Left Panel):** Learners build a binary tree. This anchors their understanding of tree structure.
2.  **Explore Traversal (Right Panel):** Select a traversal method and visualize its execution on the constructed tree.
3.  **Experiment with Insertion and Deletion (Right Panel):** Add or remove nodes and observe the changes.
4.  **Observe Properties (Right Panel):** See how the tree properties change dynamically as the tree is modified.
5.  **Tree Types (Right Panel):** select an example of a tree type, and visualize what makes the tree special.

Learner progression is driven by interaction. No explicit navigation is required.  The left panel acts as the input, and the right panel as the dynamic output/visualization area.

### ✨ Subtle Engagement Elements

*   **Hover Hints:** Hovering over nodes in the traversal visualization could display the order number in which the node is visited.
*   **Animated Transitions:** Smooth transitions when nodes are added, deleted, or highlighted during traversal to improve visual clarity.
*   **Guided Tooltips:**  A tooltip that initially highlights the interactive elements in each panel on first load. "Build Your Tree", "Choose Traversal". Dismissed automatically after a brief period or on user interaction.
*   **Colour Coding:** Colour code nodes based on their depth or level.
```