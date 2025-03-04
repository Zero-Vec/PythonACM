# https://www.lanqiao.cn/problems/156/learning/?page=1&first_category_id=1&name=%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5
n, m = map(int, input().split())
r, c = map(int, input().split())

ans = [[0] * m for _ in range(n)]

x, y = 0, 0
value = 1
ans[x][y] = value
while value < n * m:
    # 向右走
    while y + 1 < m and  ans[x][y + 1] == 0:
        value += 1
        y += 1
        ans[x][y] = value
    # 向下走
    while x + 1 < n and  ans[x + 1][y] == 0:
        value += 1
        x += 1
        ans[x][y] = value
    # 向左走
    while y - 1 >= 0 and  ans[x][y - 1] == 0:
        value += 1
        y -= 1
        ans[x][y] = value
    # 向上走
    while x - 1 >= 0 and  ans[x - 1][y] == 0:
        value += 1
        x -= 1
        ans[x][y] = value
# for i in range(n):
#     for j in range(m):
#         print(ans[i][j], end=" ")
#     print()
print(ans[r - 1][c - 1])
