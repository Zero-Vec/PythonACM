# https://www.lanqiao.cn/problems/216/learning/?page=1&first_category_id=1&problem_id=216
from functools import lru_cache
mod = 1000000007

@lru_cache(maxsize=None)
def dfs(x, y, z, mx_val):
    """
    :param x: 当前横坐标
    :param y: 当前纵坐标
    :param z: 当前个数
    :param mx_val: 当前最大价值
    :return:
    """
    if z > k:
        return 0
    if x == n - 1 and y == m - 1:
        if z == k:
            return 1
        if z == k - 1 and mx_val < mp[x][y]:
            return 1
        return 0

    ans = 0
    # 加上两个方向的方案数
    for dx, dy in [(1, 0), (0, 1)]:
        xx, yy = x + dx, y + dy
        if xx < n and yy < m:
            # 不拿当前值
            ans = (ans + dfs(xx, yy, z, mx_val)) % mod
            # 拿当前值
            if mx_val < mp[x][y]:
                ans = (ans + dfs(xx, yy, z + 1, mp[x][y])) % mod
    return ans

n, m, k = map(int, input().split())
mp = []
for i in range(n):
    mp.append(list(map(int, input().split())))
res = dfs(0, 0, 0, -1)
print(res)
