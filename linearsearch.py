# Linear Search

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Input
arr = list(map(int, input("Enter the array elements: ").split()))
key = int(input("Enter the element to search: "))

# Function Call
result = linear_search(arr, key)

# Output
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")

"""
Output:
Enter the array elements: 5 32 1 34 3
Enter the element to search: 34
Element found at index 3.
"""

"""
Algorithm: Linear Search
- Objective: Find the position of a target element in an unsorted array.
- Steps: Start from index 0, compare with target, return index if found, else -1.

Output:
Enter the array elements: 5 32 1 34 3
Enter the element to search: 34
Element found at index 3.
"""