# https://www.lanqiao.cn/problems/153/learning/?page=1&first_category_id=1&tag_relation=intersection&name=%E6%B4%81%E5%87%80%E6%95%B0
n = int(input())
ans = 0
for i in range(1, n + 1):
    if '2' not in str(i):
        ans += 1
print(ans)