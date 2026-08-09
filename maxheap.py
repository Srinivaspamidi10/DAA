import heapq

def max_heap_sort(arr):
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    sorted_arr = [-heapq.heappop(max_heap) for _ in range(len(arr))]
    return sorted_arr

if __name__ == "__main__":
    arr = [20, 25, 60, 45, 2]
    print("Enter the array elements:", " ".join(map(str, arr)))
    sorted_arr = max_heap_sort(arr)
    print("Sorted array:", sorted_arr)
