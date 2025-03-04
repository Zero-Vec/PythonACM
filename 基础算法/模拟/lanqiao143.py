# https://www.lanqiao.cn/problems/143/learning/?page=1&first_category_id=1&name=%E9%A5%AE%E6%96%99%E6%8D%A2%E8%B4%AD
n = int(input())
ans = n
while n >= 3:
    ans += n // 3
    n = n // 3 + n % 3
print(ans)
