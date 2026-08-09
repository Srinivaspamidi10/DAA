def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]

arr = [46, 18, 52, 32, 21]

selection_sort(arr)

print(arr)

"""
Output:
[18, 21, 32, 46, 52]
"""