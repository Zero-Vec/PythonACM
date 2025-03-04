# https://www.lanqiao.cn/problems/549/learning/?page=1&first_category_id=1&tag_relation=intersection&name=%E6%89%AB%E9%9B%B7
n, m = map(int, input().split())
def input_list():
    return list(map(int, input().split()))
a = []
for i in range(n):
    a.append(input_list())
b = [[0] * m for _ in range(n)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]
# 枚举第 i 行，枚举第 j 列 <i, j>
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            b[i][j] = 9
        else:
            for k in range(8):
                x, y = i + dir[k][0], j + dir[k][1]
                if 0 <= x < n and 0 <= y < m:
                    if a[x][y] == 1:
                        b[i][j] += 1
        print(b[i][j], end=' ')
    print()
