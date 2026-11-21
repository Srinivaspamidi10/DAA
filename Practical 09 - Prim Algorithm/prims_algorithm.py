import heapq
def prims_algorithm(num_vertices, edges):
    adj_list = {i: [] for i in range(num_vertices)}
    for weight, u, v in edges:
        adj_list[u].append((weight, v))
        adj_list[v].append((weight, u))
    visited = set()
    min_heap = [(0, 0, -1)]

    mst_edges = []
    total_weight = 0

    while min_heap and len(visited) < num_vertices:
        weight, u, parent = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)

        if parent != -1:
            mst_edges.append((parent, u, weight))
            total_weight += weight

        for neighbor_weight, v in adj_list[u]:
            if v not in visited:
                heapq.heappush(min_heap, (neighbor_weight, v, u))

    return total_weight, mst_edges

if __name__ == "__main__":
    n = 5

    graph_edges = [
        (2, 0, 1),
        (3, 0, 3),
        (1, 1, 2),
        (1, 1, 3),
        (4, 2, 4),
        (5, 3, 4)
    ]

    mst_cost, mst = prims_algorithm(n, graph_edges)

    print(f"Total Cost of MST: {mst_cost}")
    print("Edges in the MST (u, v, weight):")
    for u, v, weight in mst:
        print(f"({u} -- {v}) with weight {weight}")