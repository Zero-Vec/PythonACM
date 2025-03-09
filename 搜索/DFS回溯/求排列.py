def dfs(depth):
    if depth == n:
        print(path)

    for i in range(1, n + 1):
        if vis[i]:
            continue
        vis[i] = True
        path.append(i)
        dfs(depth + 1)
        vis[i] = False
        path.pop(-1)

    return

n = int(input())
path = []
vis = [False for _ in range(n + 1)]
# print(vis)
dfs(0)
