# 🕸️ Adjacency List to Matrix Converter
 
Converts a graph represented as an adjacency list into an adjacency matrix.
 
## 💡 Concept
 
A graph can be represented in two main ways:
 
- **Adjacency list** — each node maps to a list of its neighbors. Space-efficient for sparse graphs.
- **Adjacency matrix** — an n×n grid where `matrix[i][j] = 1` if an edge exists between node `i` and node `j`, `0` otherwise.
This converter takes a dictionary (adjacency list) and produces the equivalent matrix representation.
 
## 🚀 Usage
 
```python
adjacency_list = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}
adjacency_list_to_matrix(adjacency_list)
```
 
Output:
 
```
[0, 1, 1, 0]
[0, 0, 1, 0]
[1, 0, 0, 1]
[0, 0, 1, 0]
```
 
## 📊 Complexity
 
| | Adjacency List | Adjacency Matrix |
|---|---|---|
| **Space** | O(V + E) | O(V²) |
| **Edge lookup** | O(degree) | O(1) |
| **Best for** | Sparse graphs | Dense graphs |
 
## 🛠️ Tech
 
- Python 3
- No external libraries
 
