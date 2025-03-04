# https://www.lanqiao.cn/problems/2109/learning/?page=1&first_category_id=1&problem_id=2109
# 用二维前缀和暴力的方法 O(n^4) 过 70% 测试点
n, m, k = map(int, input().split())
a = [[0] * (m + 1) for _ in range(n + 1)]
sum = [[0] * (m + 1) for _ in range(n + 1)]

def get_sum(sum, x1, y1, x2, y2):
    return sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1]

for i in range(1, n + 1):
    a[i] = [0] + list(map(int, input().split()))

# 处理二维前缀和
for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + a[i][j]
ans = 0
# 枚举左上角
for x1 in range(1, n + 1):
    for y1 in range(1, m + 1):
        # 枚举右下角
        for x2 in range(x1, n + 1):
            for y2 in range(y1, m + 1):
                if get_sum(sum, x1, y1, x2, y2) <= k:
                    ans += 1
print(ans)