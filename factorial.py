import sys

sys.set_int_max_str_digits(20000)
sys.setrecursionlimit(10000)


def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial using Iterative Method:", factorial_iterative(num))
    print("Factorial using Recursive Method:", factorial_recursive(num))

"""
Output:
Enter a number: 7
Factorial using Iterative Method: 5040
Factorial using Recursive Method: 5040
"""

"""
Algorithm: Factorial (Iterative & Recursive)
- Objective: Find the factorial of a given number n.
- Steps: Iterative multiplies from 1 to n; Recursive returns n * factorial(n-1) with base case n=0 or 1.

Output:
Enter a number: 7
Factorial using Iterative Method: 5040
Factorial using Recursive Method: 5040
"""