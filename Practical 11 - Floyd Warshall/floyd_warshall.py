def floyd_warshall(graph):
    vertices = len(graph)
    distance = [row.copy() for row in graph]
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j],
                                     distance[i][k] + distance[k][j])
    return distance


if __name__ == "__main__":
    vertices = int(input("Enter number of vertices: "))
    graph = []
    print("Enter the adjacency matrix; use 99999 for infinity:")
    for i in range(vertices):
        graph.append(list(map(int, input(f"Row {i}: ").split())))
    if len(graph) != vertices or any(len(row) != vertices for row in graph):
        print("Invalid matrix dimensions.")
    else:
        distance = floyd_warshall(graph)
        print("All-pairs shortest distances:")
        for row in distance:
            print(*row)
