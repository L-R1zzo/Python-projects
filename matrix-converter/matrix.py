def adjacency_list_to_matrix(adj_list: dict):

    n = len(adj_list)
    matrix = [[0]*n for _ in range(n)]
    for node, edges in adj_list.items():
        for edge in edges:
            matrix[node][edge] = 1

    printed_matrix = ""
    for rows in matrix:
        printed_matrix += f"{rows}\n"
    print(printed_matrix)
    return matrix
        
    
if __name__ == "__main__":
    adjacency_list = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}
    adjacency_list_to_matrix(adjacency_list)
