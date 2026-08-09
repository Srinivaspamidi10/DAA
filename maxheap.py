def heapify(arr, n, i):
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < n and arr[left] > arr[largest]:
    largest = left

  if right < n and arr[right] > arr[largest]:
    largest = right

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)


def heap_sort(arr):
  n = len(arr)

  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)


arr = list(map(int, input("Enter the array elements: ").split()))
heap_sort(arr)
print("Sorted array:", arr)

"""
Output:
Enter the array elements: 20 25 60 45 2
Sorted array: [2, 20, 25, 45, 60]
"""

"""
Algorithm: Max Heap Sort
- Objective: Sort an array by building a Max Heap and extracting elements.
- Steps: Convert array to max heap, extract root (maximum), heapify, repeat.

Output:
Enter the array elements: 20 25 60 45 2
Sorted array: [2, 20, 25, 45, 60]
"""