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



if __name__ == "__main__":
    matrix = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
    ]
    print(dfs(matrix, 1))
