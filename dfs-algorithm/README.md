# Depth-First Search (DFS) — Adjacency Matrix
 
A clean Python implementation of the **Depth-First Search** graph traversal algorithm using an adjacency matrix representation.
 
---
 
## How It Works
 
DFS explores a graph by going as deep as possible along each branch before backtracking. This implementation uses an **iterative approach with an explicit stack**, avoiding recursion limits on large graphs.
 
### Algorithm Steps
 
1. Push the `start_node` onto the stack and mark it as visited.
2. Pop the top node from the stack.
3. For each neighbor of the current node, if there is an edge (`1` in the matrix) and the neighbor hasn't been visited yet, push it onto the stack.
4. Repeat until the stack is empty.
---
 
## Code
 
```python
def dfs(adj_matrix: list, start_node):
    stack = [start_node]
    visited = []
    while len(stack) > 0:
        current = stack.pop()
        visited.append(current)
        for index, edge in enumerate(adj_matrix[current]):
            if edge == 1 and not index in visited:
                stack.append(index)
    return visited
```
 
---
 
## Adjacency Matrix
 
The graph is represented as a square matrix where `matrix[i][j] = 1` means there is an edge between node `i` and node `j`.
 
### Example Graph
 
```
matrix = [
    [0, 1, 0, 0],  # node 0 → connected to 1
    [1, 0, 1, 0],  # node 1 → connected to 0, 2
    [0, 1, 0, 1],  # node 2 → connected to 1, 3
    [0, 0, 1, 0],  # node 3 → connected to 2
]
```
 
Visually:
 
```
0 ── 1
     |
     2
     |
     3
```
 
---
 
## Usage
 
```python
if __name__ == "__main__":
    matrix = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
    ]
    print(dfs(matrix, 1))  # Starting from node 1
```
 
**Output:**
```
[1, 2, 3, 0]
```
 
---
 
## Complexity
 
| | Complexity |
|---|---|
| **Time** | O(V²) — every node checks all V entries in its row |
| **Space** | O(V) — for the stack and visited list |
 
> An adjacency **list** representation would reduce time complexity to O(V + E), which is more efficient for sparse graphs.
 
---
 
## Parameters
 
| Parameter | Type | Description |
|---|---|---|
| `adj_matrix` | `list[list[int]]` | Square adjacency matrix representing the graph |
| `start_node` | `int` | Index of the node where traversal begins |
 
**Returns:** a list of node indices in the order they were visited.
 
---
 
## When to Use DFS
 
- Detecting cycles in a graph
- Topological sorting
- Solving mazes and puzzles
- Finding connected components
- Path finding between two nodes
