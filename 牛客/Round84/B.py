n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 1):
    ans += a[i + 1] - a[i]
b = sorted(a, reverse=True)
# print(b)
if a != b:
    print(2, end=' ')
else:
    print(1, end=' ')
print(ans)