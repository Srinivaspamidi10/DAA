import time


def bubble_sort(values):
    result = values.copy()
    for i in range(len(result)):
        swapped = False
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(values):
    result = values.copy()
    for i in range(len(result)):
        minimum = i
        for j in range(i + 1, len(result)):
            if result[j] < result[minimum]:
                minimum = j
        result[i], result[minimum] = result[minimum], result[i]
    return result


def insertion_sort(values):
    result = values.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def merge_sort(values):
    if len(values) <= 1:
        return values.copy()
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def quick_sort(values):
    if len(values) <= 1:
        return values.copy()
    pivot = values[len(values) // 2]
    left = [value for value in values if value < pivot]
    middle = [value for value in values if value == pivot]
    right = [value for value in values if value > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def timed_sort(sort_function, values):
    start = time.perf_counter_ns()
    sorted_values = sort_function(values)
    elapsed = time.perf_counter_ns() - start
    return sorted_values, elapsed


if __name__ == "__main__":
    values = list(map(int, input("Enter integers separated by spaces: ").split()))
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
    ]
    for name, algorithm in algorithms:
        sorted_values, elapsed = timed_sort(algorithm, values)
        print(f"{name}: {sorted_values}")
        print(f"Execution time: {elapsed} ns")
