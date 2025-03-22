# https://www.lanqiao.cn/problems/3819/learning/?page=1&first_category_id=1&problem_id=3819
from collections import deque

def bfs(x, y, dist):
    """
    :param x: 当前点横坐标
    :param y: 当前点纵坐标
    :param dist: 起点或终点到任意点的最短距离
    :return:
    """
    q = deque()
    q.append([x, y])
    dist[x][y] = 0
    vis = [[0] * m for _ in range(n)]
    vis[x][y] = 1
    while len(q) > 0:
        u, v = q.popleft()
        # vis[u][v] = 1
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            xx, yy = u + dx, v + dy
            # 判断是否越界、是否走过、是否为'#'
            if 0 <= xx < n and 0 <= yy < m and vis[xx][yy] == 0 and mp[xx][yy] != '#':
                dist[xx][yy] = dist[u][v] + 1
                q.append([xx, yy])
                vis[xx][yy] = 1
    return

n, m = map(int, input().split())
A, B, C, D = map(int, input().split())
A, B, C, D = A - 1, B - 1, C - 1, D - 1
mp = []
for i in range(n):
    mp.append(list(input()))
E = int(input())
# print(mp)
inf = 2e9
# dis1 表示起点到任意点的最短距离，dis2 表示终点到任意点的最短距离
dis1 = [[inf] * m for _ in range(n)]
dis2 = [[inf] * m for _ in range(n)]
bfs(A, B, dis1)
bfs(C, D, dis2)
ans = dis1[C][D]
# print(ans)
if ans == inf:
    print('No')
else:
    if ans <= E:
        print(ans)
    else:
        res = inf
        # 枚举每个圣水位置
        for i in range(n):
            for j in range(m):
                if mp[i][j] == 'V' and dis1[i][j] <= E:
                    res = min(res, dis1[i][j] + dis2[i][j])
        # 初始有 E，总共是 res，圣水到终点需要 res - E，加上等待时间，则需要两倍
        if res == inf:
            print('No')
        else:
            print(E + (res - E) * 2)
