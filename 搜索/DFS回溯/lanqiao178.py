# https://www.lanqiao.cn/problems/178/learning/?page=1&first_category_id=1&problem_id=178

import sys
sys.setrecursionlimit(1000000)

# 计算岛屿（连通块）数目，并且判断是否有没有被完全淹没的陆地
def dfs(x, y):
    vis[x][y] = 1
    # 判断是不是没有被完全淹没的陆地
    if mp[x - 1][y] == '#' and mp[x + 1][y] == '#' and mp[x][y - 1] == '#' and mp[x][y + 1] == '#':
        global tag
        tag = True
    # dfs 连通块
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xx, yy = x + dx, y + dy
        if mp[xx][yy] == '#' and vis[xx][yy] == 0:
            dfs(xx, yy)

    return


n = int(input())
mp = []
vis = []
for i in range(n):
    mp.append(list(input()))
    vis.append([0] * n)
ans = 0     # 表示被完全淹没的数量
for i in range(n):
    for j in range(n):
        if mp[i][j] == '#' and vis[i][j] == 0:
            tag = False
            dfs(i, j)
            if not tag:
                ans += 1
print(ans)