# https://www.lanqiao.cn/problems/1372/learning/?page=1&first_category_id=1&problem_id=1372
# 找出最短区间长度使得区间和大于或等于S
n, S = map(int, input().split())
a = list(map(int, input().split()))
# [l, r)
l, r = 0, 0
# sum 表示滑动窗口 [l, r) 之间的区间和
sum = 0
ans = n + 1
while l < n:
    # 不断扩展右端点，直到区间和 >= S
    while r < n and sum < S:
        sum += a[r]
        r += 1
    if sum >= S:
        ans = min(ans, r - l)
    # 左端点向右一步
    sum -= a[l]
    l += 1
if ans == n + 1:
    ans = 0
print(ans)
