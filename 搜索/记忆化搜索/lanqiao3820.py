# https://www.lanqiao.cn/problems/3820/learning/?page=1&first_category_id=1&problem_id=3820
from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(x, y, cnt):
    if x == C - 1 and y == D - 1:
        return True
    for dx, dy in dir:
        xx, yy = x + dx, y + dy
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if mp[xx][yy] < mp[x][y]:
            if dfs(xx, yy, cnt):
                return True
        if mp[xx][yy] < mp[x][y] + k and cnt == 1:
            if dfs(xx, yy, 0):
                return True
    return False

n, m, k = map(int, input().split())
A, B, C, D = map(int, input().split())
mp = []
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i in range(n):
    mp.append(list(map(int, input().split())))
if dfs(A - 1, B - 1, 1):
    print("Yes")
else:
    print("No")
