# https://www.lanqiao.cn/problems/199/learning/?page=1&first_category_id=1&problem_id=199
n, k = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))
a.sort()

def check(x):
    pos = 0
    # pos 表示已清理的区域为 1 ~ pos
    for i in range(k):
        t = x
        if pos < a[i]:
            t -= 2 * (a[i] - pos - 1)
        if t < 0:
            return False
        pos = a[i] + t // 2
    return pos >= n

ans = 0
l, r = 1, 2 * n
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)
