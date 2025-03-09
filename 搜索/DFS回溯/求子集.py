def dfs(depth):
    if depth == n:
        print(path)
        return

    # 选 和 不选
    path.append(a[depth])
    dfs(depth + 1)
    path.pop(-1)

    dfs(depth + 1)

n = int(input())
a = list(map(int, input().split()))
path = []
dfs(0)
