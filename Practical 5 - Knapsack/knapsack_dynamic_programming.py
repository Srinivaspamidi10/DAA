def knapsack(weights, values, capacity):
    item_count = len(values)
    table = [[0] * (capacity + 1) for _ in range(item_count + 1)]
    for i in range(1, item_count + 1):
        for current_capacity in range(capacity + 1):
            if weights[i - 1] <= current_capacity:
                included = values[i - 1] + table[i - 1][current_capacity - weights[i - 1]]
                table[i][current_capacity] = max(included, table[i - 1][current_capacity])
            else:
                table[i][current_capacity] = table[i - 1][current_capacity]

    selected = []
    current_capacity = capacity
    for i in range(item_count, 0, -1):
        if table[i][current_capacity] != table[i - 1][current_capacity]:
            selected.append(i - 1)
            current_capacity -= weights[i - 1]
    return table[item_count][capacity], list(reversed(selected))


if __name__ == "__main__":
    item_count = int(input("Enter number of items: "))
    values = list(map(int, input("Enter item values separated by spaces: ").split()))
    weights = list(map(int, input("Enter item weights separated by spaces: ").split()))
    capacity = int(input("Enter knapsack capacity: "))
    if len(values) != item_count or len(weights) != item_count:
        print("Number of values and weights must match number of items.")
    else:
        maximum_value, selected_items = knapsack(weights, values, capacity)
        print("Maximum value:", maximum_value)
        print("Selected item indexes (0-based):", selected_items)
