# https://www.lanqiao.cn/problems/3891/learning/?page=1&first_category_id=1&problem_id=3891

import sys
sys.setrecursionlimit(100000)

def dfs(x):
    vis[x] = 1
    dis[x][0] = -1
    for y in g[x]:
        if vis[y]:
            continue
        dfs(y)
        dis[x][0] += dis[y][0]
    return


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
rudu = [0] * (n + 1)
vis = [0] * (n + 1)
# 分别表示子树的数量 和 序号
dis = [[0, i] for i in range(n + 1)]
# 找根 入度为 0 的即为根
for _ in range(n - 1):
    l, r = map(int, input().split())
    g[r].append(l)
    rudu[l] += 1
# print(g)
for i in range(1, n + 1):
    if rudu[i] == 0:
        root = i

dfs(root)
dis.sort()
# print(dis)
for i, (x, y) in enumerate(dis, 1):
    if y == m:
        print(i)
        break