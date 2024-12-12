def create_adjacency_list(V, edges):
    adjacency_list = [[] for _ in range(V)]

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)  # For undirected graphs

    return adjacency_list

# New example
V = 6
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 5)]

adjacency_list = create_adjacency_list(V, edges)
print(adjacency_list)