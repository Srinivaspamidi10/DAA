def knapsack(values, weights, capacity):
  n = len(values)
  dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

  for i in range(1, n + 1):
    for w in range(capacity + 1):
      if weights[i - 1] <= w:
        dp[i][w] = max(
            values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
        )
      else:
        dp[i][w] = dp[i - 1][w]

  return dp[n][capacity]


while True:
  try:
    n = int(input("Enter the number of items: "))
    break
  except ValueError:
    print("Invalid input. Please enter a valid integer.")

values = []
weights = []

print("\nEnter value and weight of each item:")
for i in range(n):
  while True:
    try:
      value = int(input(f"Value of item {i + 1}: "))
      weight = int(input(f"Weight of item {i + 1}: "))
      break
    except ValueError:
      print("Invalid input. Please enter valid integers for value and weight.")
  values.append(value)
  weights.append(weight)

while True:
  try:
    capacity = int(input("\nEnter the knapsack capacity: "))
    break
  except ValueError:
    print("Invalid input. Please enter a valid integer for capacity.")

max_profit = knapsack(values, weights, capacity)
print("\nMaximum Profit =", max_profit)