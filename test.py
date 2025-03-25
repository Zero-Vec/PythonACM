def countLAN(s):
    n = len(s)

    dp = [[0] * 3 for _ in range(n + 1)]

    for i in range(1, n + 1):
        char = s[i - 1]

        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        dp[i][2] = dp[i - 1][2]

        if char == 'l':
            dp[i][0] += 1
        elif char == 'a':
            dp[i][1] += dp[i - 1][0]
        elif char == 'n':
            dp[i][2] += dp[i - 1][1]

    return dp[n][2]


print(countLAN(input()))