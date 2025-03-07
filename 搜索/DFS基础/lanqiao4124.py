ans = 0
def dfs(depth, n, m):
    if  n < 0 or m < 0:
        return
    if depth == 7:
        if n == 0 and m == 0:
            global ans
            ans += 1
        return
    # 分别枚举该层选择两种糖果多少个
    for i in range(6):
        for j in range(6):
            if 2 <= i + j <= 5:
                dfs(depth + 1, n - i, m - j)

dfs(0, 9, 16)
print(ans)
