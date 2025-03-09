# https://www.lanqiao.cn/problems/3075/learning/?page=1&first_category_id=1&problem_id=3075

# n边形成立条件：最小n-1条边大于最大的第n边，等价于n条边之和大于 2 * 第n边边长，用个 tot 记录当前边长总和
import sys
input = sys.stdin.readline

def dfs(depth, last_val, tot, mul):
    """
    :param depth: n边形的第depth条边
    :param last_val:选取的上一条边的值
    :param tot:当前边长总和
    :param mul:当前乘积
    :return:
    """
    if depth == n:
        if tot > 2 * path[-1]:
            ans[mul] += 1
            return
        return
    # 枚举第 depth 条边为 i
    for i in range(last_val + 1, 100001):
        if mul * (i ** (n - depth)) <= 100000:
            path.append(i)
            dfs(depth + 1, i, tot + i, mul * i)
            path.pop()
        else:
            break

    return

t, n = map(int, input().split())
path = []
ans = [0] * 100001
dfs(0, 0, 0, 1)
for i in range(1, 100001):
    ans[i] += ans[i - 1]
for _ in range(t):
    l, r = map(int, input().split())
    print(ans[r] - ans[l - 1])