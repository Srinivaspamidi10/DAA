def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [18, 57, 43, 63, 29, 22, 12]

merge_sort(arr)

print(arr)

"""
Output:
[12, 18, 22, 29, 43, 57, 63]
"""

"""
Algorithm: Merge Sort
- Objective: Sort an array using Divide and Conquer.
- Steps: Divide array into halves, recursively sort them, then merge sorted halves.

Output:
[12, 18, 22, 29, 43, 57, 63]
"""