def matrix_chain_order(dimensions):
    count = len(dimensions) - 1
    costs = [[0] * count for _ in range(count)]
    splits = [[0] * count for _ in range(count)]
    for chain_length in range(2, count + 1):
        for i in range(count - chain_length + 1):
            j = i + chain_length - 1
            costs[i][j] = float("inf")
            for k in range(i, j):
                cost = (costs[i][k] + costs[k + 1][j]
                        + dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                if cost < costs[i][j]:
                    costs[i][j] = cost
                    splits[i][j] = k

    def print_parentheses(i, j):
        if i == j:
            return f"A{i + 1}"
        k = splits[i][j]
        return "(" + print_parentheses(i, k) + " " + print_parentheses(k + 1, j) + ")"

    return int(costs[0][count - 1]), print_parentheses(0, count - 1)


if __name__ == "__main__":
    dimensions = list(map(int, input("Enter matrix dimensions separated by spaces: ").split()))
    if len(dimensions) < 2:
        print("Enter at least two dimensions.")
    else:
        minimum_cost, parenthesization = matrix_chain_order(dimensions)
        print("Minimum scalar multiplications:", minimum_cost)
        print("Parenthesization:", parenthesization)
