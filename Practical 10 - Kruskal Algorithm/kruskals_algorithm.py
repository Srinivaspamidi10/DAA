class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True


def kruskals_mst(vertices, edges):
    disjoint_set = DisjointSet(vertices)
    mst_edges = []
    total_weight = 0
    for weight, u, v in sorted(edges):
        if disjoint_set.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == vertices - 1:
                break
    if len(mst_edges) != vertices - 1:
        return None, mst_edges
    return total_weight, mst_edges


if __name__ == "__main__":
    vertices = int(input("Enter number of vertices: "))
    edge_count = int(input("Enter number of edges: "))
    edges = []
    for _ in range(edge_count):
        u, v, weight = map(int, input("Enter edge (u v weight): ").split())
        edges.append((weight, u, v))
    total, mst = kruskals_mst(vertices, edges)
    if total is None:
        print("Graph is disconnected; MST does not exist.")
    else:
        print("Minimum spanning tree edges:", mst)
        print("Total weight:", total)
