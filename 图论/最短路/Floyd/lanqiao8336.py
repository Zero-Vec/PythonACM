# https://www.lanqiao.cn/problems/8336/learning/?page=1&first_category_id=1&problem_id=8336
n, m = map(int, input().split())
a, p, s = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    a[i], p[i], s[i] = map(int, input().split())
inf = 1e18
f = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    f[u][v] = min(f[u][v], w)
    f[v][u] = f[u][v]
for i in range(1, n + 1):
    f[i][i] = 0
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            f[i][j] = min(f[i][j], f[i][k] + f[k][j])
g = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        g[i][j] = s[j] - p[i] - f[i][j]
ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        tmp = max(tmp, g[i][j])
    ans += tmp * a[i]
print(ans)
