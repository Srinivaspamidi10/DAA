from collections import deque


class Graph:
    def __init__(self, vertices):
        self.adjacency = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency[u].append(v)
        self.adjacency[v].append(u)

    def dfs(self, start):
        visited = [False] * len(self.adjacency)
        order = []
        def visit(vertex):
            visited[vertex] = True
            order.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if not visited[neighbor]:
                    visit(neighbor)
        visit(start)
        return order

    def bfs(self, start):
        visited = [False] * len(self.adjacency)
        queue = deque([start])
        visited[start] = True
        order = []
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return order


if __name__ == "__main__":
    vertices = int(input("Enter number of vertices: "))
    graph = Graph(vertices)
    edge_count = int(input("Enter number of edges: "))
    for _ in range(edge_count):
        u, v = map(int, input("Enter edge (u v): ").split())
        graph.add_edge(u, v)
    start = int(input("Enter start vertex: "))
    print("DFS:", *graph.dfs(start))
    print("BFS:", *graph.bfs(start))
