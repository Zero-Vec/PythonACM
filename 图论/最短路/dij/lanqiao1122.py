# https://www.lanqiao.cn/problems/1122/learning/?page=1&first_category_id=1&problem_id=1122
from queue import PriorityQueue

def dij(st):
    dis[st] = 0
    pq = PriorityQueue()
    # vis 表示是否出队，如果是 bfs 中的标记数组是表示是否入队
    vis = [0] * (n + 1)
    pq.put((dis[st], st))
    while not pq.empty():
        d, x = pq.get()
        if vis[x]:continue
        vis[x] = 1
        for v, w in g[x]:
            if vis[v]:continue
            if dis[v] > dis[x] + w:
                dis[v] = dis[x] + w
                pq.put((dis[v], v))
    return

n, m = map(int, input().split())
g = [[] for i in range(n + 1)]
inf = 1e18
dis = [inf] * (n + 1)
for i in range(m):
    u, v, w = map(int, input().split())
    g[u].append([v, w])
dij(1)
for i in range(1, n + 1):
    if dis[i] == inf:
        dis[i] = -1
print(*dis[1::])
