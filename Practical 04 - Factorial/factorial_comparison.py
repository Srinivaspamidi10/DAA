import time


def factorial_iterative(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def factorial_recursive(number):
    if number in (0, 1):
        return 1
    return number * factorial_recursive(number - 1)


if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative integers.")
    else:
        start = time.perf_counter_ns()
        iterative_result = factorial_iterative(number)
        iterative_time = time.perf_counter_ns() - start
        start = time.perf_counter_ns()
        recursive_result = factorial_recursive(number)
        recursive_time = time.perf_counter_ns() - start
        print("Iterative result:", iterative_result)
        print("Iterative time:", iterative_time, "ns")
        print("Recursive result:", recursive_result)
        print("Recursive time:", recursive_time, "ns")
