def traveling_salesman(graph):
    vertices = len(graph)
    if vertices == 0:
        return 0, []
    if vertices == 1:
        return 0, [0]

    infinity = float("inf")
    dp = {}
    parent = {}

    def solve(mask, current):
        if mask == (1 << 0) | sum(1 << city for city in range(1, vertices)):
            return graph[current][0]
        key = (mask, current)
        if key in dp:
            return dp[key]

        best = infinity
        best_next = -1
        for next_city in range(1, vertices):
            if mask & (1 << next_city):
                continue
            next_mask = mask | (1 << next_city)
            cost = graph[current][next_city] + solve(next_mask, next_city)
            if cost < best:
                best = cost
                best_next = next_city
        dp[key] = best
        parent[key] = best_next
        return best

    full_mask = (1 << vertices) - 1
    best_cost = solve(1, 0)
    if best_cost == infinity:
        return None, []

    path = [0]
    mask = 1
    current = 0
    while mask != full_mask:
        next_city = parent[(mask, current)]
        path.append(next_city)
        mask |= 1 << next_city
        current = next_city
    path.append(0)
    return int(best_cost), path


if __name__ == "__main__":
    vertices = int(input("Enter number of cities: "))
    graph = []
    print("Enter the cost matrix; use 0 for a city to itself:")
    for i in range(vertices):
        graph.append(list(map(int, input(f"Row {i}: ").split())))
    if len(graph) != vertices or any(len(row) != vertices for row in graph):
        print("Invalid matrix dimensions.")
    else:
        cost, path = traveling_salesman(graph)
        if cost is None:
            print("No Hamiltonian cycle exists.")
        else:
            print("Minimum tour cost:", cost)
            print("Tour:", " -> ".join(map(str, path)))
