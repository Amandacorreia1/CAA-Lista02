def palindroma_maxima(s):
    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    max_length = 1
    start = 0
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                start = i
    return s[start:start + max_length]

s = "ACGTGTCAAAATCGAAMMAA"
print("\tSubsequência palindrômica máxima: ")
print(palindroma_maxima(s))
