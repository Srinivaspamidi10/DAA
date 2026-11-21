def minimum_coins(amount, coins):
    table = [float("inf")] * (amount + 1)
    table[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                table[value] = min(table[value], table[value - coin] + 1)
    return None if table[amount] == float("inf") else table[amount]


def coin_change_ways(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for value in range(coin, amount + 1):
            ways[value] += ways[value - coin]
    return ways[amount]


if __name__ == "__main__":
    coins = list(map(int, input("Enter coin denominations separated by spaces: ").split()))
    amount = int(input("Enter target amount: "))
    minimum = minimum_coins(amount, coins)
    ways = coin_change_ways(amount, coins)
    print("Minimum number of coins:", minimum if minimum is not None else "No solution")
    print("Number of coin combinations:", ways)
