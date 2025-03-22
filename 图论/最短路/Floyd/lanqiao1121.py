# https://www.lanqiao.cn/problems/1121/learning/?page=1&first_category_id=1&problem_id=1121
n, m, q = map(int, input().split())
inf = 1e18
dp = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    dp[u][v] = min(dp[u][v], w)
    dp[v][u] = dp[u][v]
for i in range(1, n + 1):
    dp[i][i] = 0
# Floyd
# 枚举中转点
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
for _ in range(q):
    st, ed = map(int, input().split())
    if dp[st][ed] == inf:
        print(-1)
    else:
        print(dp[st][ed])
