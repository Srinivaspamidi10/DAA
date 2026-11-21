import heapq


def prims_mst(vertices, edges, start=0):
    adjacency = [[] for _ in range(vertices)]
    for u, v, weight in edges:
        adjacency[u].append((weight, v))
        adjacency[v].append((weight, u))
    visited = [False] * vertices
    priority_queue = [(0, start, -1)]
    mst_edges = []
    total_weight = 0
    while priority_queue:
        weight, vertex, parent = heapq.heappop(priority_queue)
        if visited[vertex]:
            continue
        visited[vertex] = True
        if parent != -1:
            mst_edges.append((parent, vertex, weight))
            total_weight += weight
        for next_weight, neighbor in adjacency[vertex]:
            if not visited[neighbor]:
                heapq.heappush(priority_queue, (next_weight, neighbor, vertex))
    if len(mst_edges) != vertices - 1:
        return None, mst_edges
    return total_weight, mst_edges


if __name__ == "__main__":
    vertices = int(input("Enter number of vertices: "))
    edge_count = int(input("Enter number of edges: "))
    edges = []
    for _ in range(edge_count):
        u, v, weight = map(int, input("Enter edge (u v weight): ").split())
        edges.append((u, v, weight))
    total, mst = prims_mst(vertices, edges)
    if total is None:
        print("Graph is disconnected; MST does not exist.")
    else:
        print("Minimum spanning tree edges:", mst)
        print("Total weight:", total)
