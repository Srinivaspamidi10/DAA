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