# https://www.lanqiao.cn/problems/3818/learning/?page=1&first_category_id=1&problem_id=3818
# print(ord('C') - ord('A'))
import sys
from queue import PriorityQueue
input = sys.stdin.readline

def cal(x, y):
    if mp[x][y] == '.':
        return 0
    else:
        return ord(mp[x][y]) - ord('A') + 1

def dij(x, y):
    dis[x][y] = 0
    vis = [[0] * m for i in range(n)]
    pq = PriorityQueue()
    pq.put((dis[x][y], x, y))
    while not pq.empty():
        d, u, v = pq.get()
        if vis[u][v] == 1:
            continue
        vis[u][v] = 1
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            xx, yy = u + dx, v + dy
            # 未标记、未越界、不为 #
            if 0 <= xx < n and 0 <= yy < m and vis[xx][yy] == 0 and mp[xx][yy] != '#':
                if dis[xx][yy] > dis[u][v] + cal(xx, yy):
                    dis[xx][yy] = dis[u][v] + cal(xx, yy)
                    pq.put((dis[xx][yy], xx, yy))
    return

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
mp = []
# dis[x][y] 表示起点到 x,y 的最短距离
inf = 1e18
dis = [[inf] * m for i in range(n)]
for i in range(n):
    mp.append(list(input()))
E = int(input())
dij(x1, y1)
if dis[x2][y2] <= E:
    print('Yes')
else:
    print('No')
