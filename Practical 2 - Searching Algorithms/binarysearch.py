def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_value = 23

    result = binary_search(sorted_array, target_value)

    print(f"Array: {sorted_array}")
    print(f"Target: {target_value}")
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")

"""
Output:
Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
Target: 23
Element found at index: 5
"""