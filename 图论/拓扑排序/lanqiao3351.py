# https://www.lanqiao.cn/problems/3351/learning/?page=1&first_category_id=1&problem_id=3351
from queue import PriorityQueue

def topo():
    q = PriorityQueue()
    for i in range(1, n + 1):
        if rudu[i] == 0:
            q.put(i)
    ans = []
    while not q.empty():
        x = q.get()
        ans.append(x)
        for y in g[x]:
            rudu[y] -= 1
            if rudu[y] == 0:
                q.put(y)
    if len(ans) != n:
        print(-1)
    else:
        print(*ans, sep=' ')

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
rudu = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    rudu[b] += 1
topo()
