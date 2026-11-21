def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    n = 7
    print(f"Enter a number: {n}")
    print(f"Factorial using Iterative Method: {factorial_iterative(n)}")
    print(f"Factorial using Recursive Method: {factorial_recursive(n)}")

"""
Output:
Enter a number: 7
Factorial using Iterative Method: 5040
Factorial using Recursive Method: 5040
"""
