# jakid 1103561 2024-12-12
from collections import deque

def bfs(adj):
    n = len(adj)
    visited = [False] * n
    bfs_order = []
    queue = deque([0])  # Start from vertex 0

    while queue:
        vertex = queue.popleft()
        if not visited[vertex]:
            visited[vertex] = True
            bfs_order.append(vertex)
            for neighbor in adj[vertex]:
                queue.append(neighbor)

    return bfs_order

# New input example
adj = [[1, 2], [0, 3, 4], [0, 4, 5], [1, 5], [1, 2, 5], [2, 3]]
bfs_order = bfs(adj)
print(bfs_order)  # Output: [0, 1, 2, 3, 4, 5]
