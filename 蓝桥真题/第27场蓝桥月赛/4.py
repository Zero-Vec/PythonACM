import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
# print(a)
b_sorted = []
ans = 0
for i in range(n):
    bisect.insort(b_sorted, b[i])
    pos = bisect.bisect_left(b_sorted, a[i])
    ans += pos
print(ans)
