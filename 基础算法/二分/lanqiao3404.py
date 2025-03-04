# https://www.lanqiao.cn/problems/3404/learning/?page=1&first_category_id=1&tag_relation=intersection&name=%E8%82%96%E6%81%A9%E7%9A%84%E4%B9%98%E6%B3%95%E8%A1%A8
# 第 k 小问题
n, m, k = map(int, input().split())
# 计算乘法矩阵中有多少个数字小于等于 x
def check(x):
    cnt = 0
    for i in range(1, n + 1):
        # 第 i 行的数字为：i,2i,3i,...,mi
        # i * j <= x => j <= x // i
        cnt += min(x // i, m)
    return cnt

# 第 k 小在区间[1, n * m]
l, r = 1, n * m
ans = -1
while l <= r:
    mid = (l + r) // 2
    # 第 k 小的数字 mid，在原数组中小于等于 mid 的数字至少有 k 个
    if check(mid) >= k:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
