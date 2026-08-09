def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [2, 54, 21, 32, 5]
    arr.sort()
    target = 21
    print("Enter the sorted array elements:", " ".join(map(str, arr)))
    print(f"Enter the element to search: {target}")
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}.")
    else:
        print("Element not found.")
