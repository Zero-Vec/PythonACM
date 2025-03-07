# https://www.lanqiao.cn/problems/3505/learning/?page=1&first_category_id=1&problem_id=3505
import sys
input = sys.stdin.readline

def dfs(depth, weight, cnt):
    global ans
    if cnt >= ans:
        return

    if weight > m:
        return

    if weight == m:
        ans = cnt
        return

    if depth == n:
        return

    # 枚举买每个瓜的情况
    dfs(depth + 1, weight, cnt)     # 不买
    dfs(depth + 1, weight + a[depth], cnt)      # 买瓜但不砍一刀
    dfs(depth + 1, weight + a[depth] // 2, cnt + 1)     # 买瓜且砍一刀

n, m = map(int, input().split())
m = m * 2
a = list(map(int, input().split()))
a = [i * 2 for i in a]
ans = n + 1
dfs(0, 0, 0)
if ans == n + 1:
    ans = -1
print(ans)
