# https://www.lanqiao.cn/problems/19715/learning/?page=1&first_category_id=1&name=%E5%9B%9E%E6%96%87%E6%95%B0%E7%BB%84
n = int(input())
a = [0] + list(map(int, input().split()))
ans = 0
for i in range(1, n // 2 + 1):
    k1 = a[i] - a[-i]
    k2 = a[i + 1] - a[-i - 1]
    if k1 * k2 <= 0:
        ans += abs(k1)
    else:
        if k1 == 0:
            continue
        elif k1 < 0:
            ans += abs(k1)
            a[i + 1] += min(abs(k1), abs(k2))
        else:
            ans += abs(k1)
            a[i + 1] -= min(abs(k1), abs(k2))
print(ans)
