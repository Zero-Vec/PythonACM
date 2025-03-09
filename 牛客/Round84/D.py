n, k = map(int, input().split())
a = list(map(lambda x:ord(x) - ord('a'), list(input())))
b = [abs(a[i + 1] - a[i]) for i in range(n - 1)]
diff = [0] * n
pre = [0] * n
for i in range(n - k + 1):
    diff[i] += 1
    diff[i + k - 1] -= 1
pre[0] = diff[0]
for i in range(1, n - 1):
    pre[i] = pre[i - 1] + diff[i]
ans = 0
for i in range(n - 1):
    ans += pre[i] * b[i]
print(ans)
