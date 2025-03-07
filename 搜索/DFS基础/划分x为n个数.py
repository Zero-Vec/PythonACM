# 增加一个枚举起点参数进行剪枝
def dfs(depth, last_val):
    # 搜索出口
    if depth == n:
        # 判断是否递增
        for i in range(1, n):
            if path[i] < path[i - 1]:
                return
        # 判断加和是否为x
        if sum(path) != x:
            return
        print(path)
        return
    # 对于每一层，枚举当前被拆分的数字
    for i in range(last_val, x + 1):
        path[depth] = i
        dfs(depth + 1, i)

x = int(input())
n = int(input())
path = [0] * n
dfs(0, 1)
