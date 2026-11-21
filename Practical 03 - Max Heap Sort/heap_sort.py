def max_heapify(values, heap_size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < heap_size and values[left] > values[largest]:
        largest = left
    if right < heap_size and values[right] > values[largest]:
        largest = right
    if largest != index:
        values[index], values[largest] = values[largest], values[index]
        max_heapify(values, heap_size, largest)


def heap_sort(values):
    result = values.copy()
    for index in range(len(result) // 2 - 1, -1, -1):
        max_heapify(result, len(result), index)
    for index in range(len(result) - 1, 0, -1):
        result[0], result[index] = result[index], result[0]
        max_heapify(result, index, 0)
    return result


if __name__ == "__main__":
    values = list(map(int, input("Enter integers separated by spaces: ").split()))
    print("Heap sorted array:", heap_sort(values))
