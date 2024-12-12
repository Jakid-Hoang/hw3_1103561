# jakid 1103561 2024-12-12
import heapq

def find_mst_weight(V, adj):
    visited = [False] * V
    pq = [(0, 0)]  # (weight, vertex)
    mst_weight = 0

    while pq:
        weight, vertex = heapq.heappop(pq)
        if visited[vertex]:
            continue
        visited[vertex] = True
        mst_weight += weight

        for neighbor, weight in adj[vertex]:
            if not visited[neighbor]:
                heapq.heappush(pq, (weight, neighbor))

    return mst_weight

# New example
V = 6
adj = [[(1, 2), (2, 4)], [(0, 2), (3, 5), (4, 3)], [(0, 4), (1, 2), (4, 1), (5, 2)], [(1, 5), (4, 1)], [(2, 1), (2, 4), (3, 1)], [(2, 2), (3, 5)]]
mst_weight = find_mst_weight(V, adj)
print("Sum of MST weights:", mst_weight)
