# jakid 1103561 2024-12-12
def dfs(adj):
    n = len(adj)
    visited = [False] * n
    dfs_order = []

    def dfs_helper(vertex):
        visited[vertex] = True
        dfs_order.append(vertex)
        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                dfs_helper(neighbor)

    dfs_helper(0)

    return dfs_order

# Example usage
adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
dfs_order = dfs(adj)
print(dfs_order)  
