from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    traversal = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))
            
    return traversal

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    traversal = []
    
    while queue:
        node = queue.popleft()
        traversal.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    start_node = 'A'
    print(f"Graph: {graph}")
    print(f"Starting Node: {start_node}")
    
    dfs_result = dfs(graph, start_node)
    bfs_result = bfs(graph, start_node)
    
    print(f"DFS Traversal: {' -> '.join(dfs_result)}")
    print(f"BFS Traversal: {' -> '.join(bfs_result)}")

"""
Output:
Graph: {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
Starting Node: A
DFS Traversal: A -> B -> D -> E -> F -> C
BFS Traversal: A -> B -> C -> D -> E -> F
"""