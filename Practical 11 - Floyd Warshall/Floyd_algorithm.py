def floydWarshall(dist):
    V = len(dist)
    INF = int(1e8)

    for k in range(V):
        for i in range(V):

            for j in range(V):

                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j],
                        dist[i][k] + dist[k][j])

if __name__ == "__main__":
    INF = int(1e8)
    dist = [[0, 4, INF, 5, INF],
            [INF, 0, 1, INF, 6],
            [2, INF, 0, 3, INF],
            [INF, INF, 1, 0, 2],
            [1, INF, INF, 4, 0]]

    floydWarshall(dist)

    for row in dist:
        print(*row)