def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

if __name__ == "__main__":
    values = [60, 100, 120, 40]
    weights = [10, 20, 30, 50]
    capacity = 60
    max_profit = knapsack(weights, values, capacity)
    print("Maximum Profit =", max_profit)

"""
Output:
Enter the number of items: 4
Enter value and weight of each item:
Value of item 1: 60, Weight of item 1: 10
Value of item 2: 100, Weight of item 2: 20
Value of item 3: 120, Weight of item 3: 30
Value of item 4: 40, Weight of item 4: 50
Enter the knapsack capacity: 60
Maximum Profit = 280
"""
