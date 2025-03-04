# https://www.lanqiao.cn/problems/550/learning/?page=1&first_category_id=1&name=%E5%9B%BE%E5%83%8F%E6%A8%A1%E7%B3%8A
n, m = map(int, input().split())
mp = []
for i in range(n):
    mp.append(list(map(int, input().split())))
ans = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        sum, cnt = 0, 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                cnt += 1
                sum += mp[x][y]
        ans[i][j] = sum // cnt

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()


