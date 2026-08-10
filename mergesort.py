def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result.extend(L[i:])
    result.extend(R[j:])
    return result

if __name__ == "__main__":
    arr = [57, 18, 22, 29, 43, 12, 63]
    print(merge_sort(arr))

"""
Output:
[12, 18, 22, 29, 43, 57, 63]
"""
