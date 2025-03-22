def solve(S):
    n = len(S)
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(4):
            dp[i][j] = dp[i - 1][j]
            if j > 0 and S[i - 1] == 'lan'[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]

    return dp[n][3]


S = input()
print(solve(S))
