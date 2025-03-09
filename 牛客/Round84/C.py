# print(ord('b') - ord('z'))
n, k = map(int, input().split())
s = list(input())
ans = 0
for i in range(n - k + 1):
    for j in range(i, i + k - 1):
        ans += abs(ord(s[j + 1]) - ord(s[j]))
print(ans)