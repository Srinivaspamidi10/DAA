from collections import deque
import time


class graph:

  def __init__(self, vertices):
    self.V = vertices
    self.adj = [[] for _ in range(vertices)]

  def addEdge(self, u, v):
    self.adj[u].append(v)
    self.adj[v].append(u)

  def DFSUtil(self, v, visited):
    visited[v] = True
    print(v, end=" ")

    for neighbor in self.adj[v]:
      if not visited[neighbor]:
        self.DFSUtil(neighbor, visited)

  def DFS(self, start):
    visited = [False] * self.V
    self.DFSUtil(start, visited)

  def BFS(self, start):
    visited = [False] * self.V
    q = deque([start])

    visited[start] = True

    while q:
      node = q.popleft()
      print(node, end=" ")

      for neighbor in self.adj[node]:
        if not visited[neighbor]:
          visited[neighbor] = True
          q.append(neighbor)


if __name__ == "__main__":
  V = int(input("Enter number of vertices: "))
  g = graph(V)

  E = int(input("Enter number of edges: "))
  print("Enter edges (u v) — enter one edge per line:")
  for _ in range(E):
    u, v = map(int, input().split())
    g.addEdge(u, v)

  start = int(input("Enter starting vertex: "))

  start_dfs = time.perf_counter_ns()
  print("\nDFS Traversal: ", end="")
  g.DFS(start)
  end_dfs = time.perf_counter_ns()
  dfs_time = end_dfs - start_dfs

  start_bfs = time.perf_counter_ns()
  print("\n\nBFS Traversal: ", end="")
  g.BFS(start)
  end_bfs = time.perf_counter_ns()
  bfs_time = end_bfs - start_bfs

  print("\n\nExecution Time:")
  print(f"DFS: {dfs_time} ns")
  print(f"BFS: {bfs_time} ns")

"""
Output:
Enter number of vertices: 5
Enter number of edges: 5
Enter edges (u v) — enter one edge per line:
0 1
0 4
1 2
1 3
1 4
Enter starting vertex: 0

DFS Traversal: 0 1 2 3 4 

BFS Traversal: 0 1 4 2 3 

Execution Time:
DFS: 124300 ns
BFS: 98100 ns
"""