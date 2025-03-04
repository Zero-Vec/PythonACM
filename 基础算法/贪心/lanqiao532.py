# https://www.lanqiao.cn/problems/532/learning/?page=1&first_category_id=1&name=%E7%BA%AA%E5%BF%B5%E5%93%81%E5%88%86%E7%BB%84
w = int(input())
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))
a.sort()

ans = 0
# print(a)
# 双指针分组
l, r = 0, n - 1
while l <= r:
    if l == r:
        ans += 1
        break
    if a[l] + a[r] <= w:
        l += 1
        r -= 1
    else:
        r -= 1
    ans += 1
print(ans)
