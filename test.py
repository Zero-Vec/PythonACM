n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
diff = [0] * (n + 9)
for i in range(1, n + 1):
    diff[i] = a[i] - a[i - 1]
for _ in range(m):
    x, y, z = map(int, input().split())
    diff[x] += z
    diff[y + 1] -= z
for i in range(1, n + 1):
    a[i] = a[i - 1] + diff[i]
    print(a[i], end=' ')