def car_assembly(a, t, e, x, n):
    f1 = [0] * n
    f2 = [0] * n
    
    f1[0] = e[0] + a[0][0]
    f2[0] = e[1] + a[1][0]
    
    for j in range(1, n):
        f1[j] = min(f1[j - 1] + a[0][j], f2[j - 1] + t[1][j - 1] + a[0][j])
        f2[j] = min(f2[j - 1] + a[1][j], f1[j - 1] + t[0][j - 1] + a[1][j])
        
    return min(f1[n - 1] + x[0], f2[n - 1] + x[1])

if __name__ == "__main__":
    a = [
        [4, 5, 3, 2],
        [2, 10, 1, 4]
    ]
    t = [
        [0, 7, 4, 5],
        [0, 9, 2, 8]
    ]
    e = [10, 12]
    x = [18, 7]
    n = len(a[0])
    
    min_time = car_assembly(a, t, e, x, n)
    print(f"Number of stations: {n}")
    print(f"Minimum time to process: {min_time}")

"""
Output:
Number of stations: 4
Minimum time to process: 35
"""