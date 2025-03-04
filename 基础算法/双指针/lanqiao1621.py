# https://www.lanqiao.cn/problems/1621/learning/?page=1&first_category_id=1&problem_id=1621
# 找有多少个区间满足：至少k个数字≥m
n, m, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 0
# [l, r)
cnt = 0
ans = 0
# cnt 表示滑动窗口[l,r)中≥m的元素个数
while l < n:
    # 不断扩展右端点，直至区间恰好有k个数字≥m
    while r < n and cnt < k:
        if a[r] >= m:
            cnt += 1
        r += 1
    if cnt >= k:
        ans += n - r + 1
    # 左端点向右一步
    if a[l] >= m:
        cnt -= 1
    l += 1
print(ans)
