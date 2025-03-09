# https://www.lanqiao.cn/problems/1508/learning/?page=1&first_category_id=1&problem_id=1508

# 深度表示枚举的当前行x
def dfs(x):
    if x == n + 1:
        global ans
        ans += 1
        return

    # 枚举当前行的所有列
    for y in range(1, n + 1):
        if vis1[y] or vis2[x + y] or vis3[x - y + n]:
            continue
        vis1[y] = vis2[x + y] = vis3[x - y + n] = True
        dfs(x + 1)
        vis1[y] = vis2[x + y] = vis3[x - y + n] = False
    return

n = int(input())
# 用三个标记数组分别表示 列、主对角线、副对角线是否被标记
vis1 = [False] * (n + 1)
vis2 = [False] * (2 * n + 1)
vis3 = [False] * (2 * n + 1)
ans = 0
dfs(1)
print(ans)
