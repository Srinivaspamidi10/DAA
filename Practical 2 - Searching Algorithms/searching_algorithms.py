import time


def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


if __name__ == "__main__":
    values = list(map(int, input("Enter integers separated by spaces: ").split()))
    target = int(input("Enter value to search: "))

    start = time.perf_counter_ns()
    linear_result = linear_search(values, target)
    linear_time = time.perf_counter_ns() - start

    sorted_values = sorted(values)
    start = time.perf_counter_ns()
    binary_result = binary_search(sorted_values, target)
    binary_time = time.perf_counter_ns() - start

    print("Linear search index:", linear_result)
    print("Linear search time:", linear_time, "ns")
    print("Binary search index in sorted array:", binary_result)
    print("Binary search time:", binary_time, "ns")
