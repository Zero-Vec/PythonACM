# https://www.lanqiao.cn/problems/182/learning/?page=1&first_category_id=1&problem_id=182

import sys
# 段错误是因为递归层数过大
# 扩栈：设置最大栈空间
sys.setrecursionlimit(100000)

# 当前点位于 x，步长为length
def dfs(x, length):
    # 记录走到 x 的步长为 length
    vis[x] = length
    # 接下来走下一个点，得判断下一个点是否被走过
    if vis[a[x]] != 0:
        # 此时存在环
        global ans
        ans = max(ans, length - vis[a[x]] + 1)
    else:
        dfs(a[x], length + 1)
    return

n = int(input())
a = [0] + list(map(int, input().split()))
vis = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    # 枚举每一个连通块，进行 dfs
    if vis[i] == 0:
        dfs(i, 1)
# print(vis)
print(ans)