# https://www.lanqiao.cn/problems/1337/learning/?page=1&first_category_id=1&problem_id=1337
from collections import deque

def topo():
    q = deque()
    for i in range(1, n + 1):
        if rudu[i] == 0:
            q.append(i)
    while len(q) > 0:
        x = q.popleft()
        for y in g[x]:
            rudu[y] -= 1
            dp[y] = max(dp[y], dp[x] + 1)
            if rudu[y] == 0:
                q.append(y)
    return

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
rudu = [0] * (n + 1)
# dp[i] 表示从入度为0的点出发得到的最远距离
dp = [0] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    rudu[v] += 1
topo()
print(max(dp))
