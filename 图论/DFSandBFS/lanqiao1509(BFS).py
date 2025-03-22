# https://www.lanqiao.cn/problems/1509/learning/?page=1&first_category_id=1&problem_id=1509

from collections import deque

def bfs(s, e):
    """
    :param s: 起点
    :param e: 终点
    :return: 次数
    """
    q = deque()
    q.append(s)
    dis[s] = 0
    while len(q) > 0:
        # 取队首
        x = q.popleft()
        if x == e:
            return dis[x]
        # 走三种情况
        for u in [x + 1, x - 1, x * 2]:
            # 判断边界和是否走过，加入队列
            if 1 <= u <= 100000 and dis[u] == -1:
                q.append(u)
                dis[u] = dis[x] + 1
    return -1

n, k = map(int, input().split())
dis = [-1] * 100009
print(bfs(n, k))
