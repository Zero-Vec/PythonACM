n = int(input())
res = []
for i in range(1, n + 1):
    a, b = map(int, input().split())
    res.append([a - b, i, a, b])
res.sort(reverse=True)
# print(res)
ans = 0
for i in range(1, n + 1):
    if i < n // 2 + 1:
        ans += res[i - 1][2]
    else:
        ans += res[i - 1][3]
print(ans)