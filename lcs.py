def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    i, j = m, n
    lcs_chars = []
    
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_chars.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    lcs_string = "".join(reversed(lcs_chars))
    return dp[m][n], lcs_string

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(f"Sequence 1: {X}")
    print(f"Sequence 2: {Y}")
    length, subsequence = lcs(X, Y)
    print(f"LCS Length: {length}")
    print(f"LCS String: {subsequence}")

"""
Output:
Sequence 1: AGGTAB
Sequence 2: GXTXAYB
LCS Length: 4
LCS String: GTAB
"""