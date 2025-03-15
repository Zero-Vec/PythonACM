# https://oj.socoding.cn/contest/problem?id=656&pid=2

def dfs(x, l, r, L, R):
    global tag
    if tag == 0:
        return
    vis[x] = 1
    for i in mp[x]:
        if vis[i] == 1:
            continue
        if i < x and ls[x] == 0 and l <= i <= r:
            ls[x] = i
            dfs(i, l, i - 1, i + 1, r)
        elif i > x and rs[x] == 0 and L <= i <= R:
            rs[x] = i
            dfs(i, L, i - 1, i + 1, R)
        else:
            tag = 0
            return
    return

n = int(input())
mp = [[] for _ in range(n + 1)]
for i in range(n - 1):
    x, y = map(int, input().split())
    mp[x].append(y)
    mp[y].append(x)
# print(mp[1])
# for i in mp[1]:
#     print(i)

vis = [0] * (n + 1)
ls = [0] * (n + 1)
rs = [0] * (n + 1)
tag = 1
ans = []
# 枚举每个点作为根节点
for i in range(1, n + 1):
    tag = 1
    vis = [0] * (n + 1)
    ls = [0] * (n + 1)
    rs = [0] * (n + 1)
    dfs(i, 1, i - 1, i + 1, n)
    if tag == 1:
        ans.append(i)
if len(ans) == 0:
    print("Impossible")
else:
    print(len(ans))
    for i in ans:
        print(i, end=' ')
