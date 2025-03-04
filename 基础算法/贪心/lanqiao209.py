# https://www.lanqiao.cn/problems/209/learning/?page=1&first_category_id=1&name=%E7%BF%BB%E7%A1%AC%E5%B8%81
s = list(input())
e = list(input())
n = len(s)
# print(s[0] == e[0])
# print(s)
ans = 0

for i in range(n):
    if s[i] == e[i]:
        continue
    if s[i + 1] == '*':
        s[i + 1] = 'o'
    else:
        s[i + 1] = '*'
    ans += 1
print(ans)
# 乘积和贪心问题：两个数组任意排序，乘积和最小。
# 贪心策略：让一个数组从大到小排序，另一个从小到大排序即可