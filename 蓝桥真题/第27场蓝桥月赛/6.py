def check(M, n, a, b, t):
    cur_t = 0
    days = 1
    if max(a) > M:
        return False
    for i in range(n):
        if cur_t + a[i] > M:
            days += 1
            cur_t = 0
            if days > t:
                return False
        # 累加当前电脑的备份时间
        cur_t += a[i]
        # 如果当前电脑不是最后一台，则累加等待时间
        if i < n - 1:
            cur_t += b[i]
            # 如果等待时间跨天，则需要新的一天
            if cur_t > M:
                tmp = cur_t - M
                days += 1
                days += tmp // M
                cur_t = tmp % M
                if days > t:
                    return False
    return days <= t

n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
left, right = 1, 3600
res = -1
while left <= right:
    mid = (left + right) // 2
    if check(mid, n, a, b, t):
        res = mid
        right = mid - 1
    else:
        left = mid + 1
print(res)
