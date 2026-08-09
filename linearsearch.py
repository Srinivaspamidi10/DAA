def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [5, 32, 1, 34, 3]
    target = 34
    print("Enter the array elements:", " ".join(map(str, arr)))
    print(f"Enter the element to search: {target}")
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}.")
    else:
        print("Element not found.")
