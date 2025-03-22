# https://www.lanqiao.cn/problems/19714/learning/?page=1&first_category_id=1&name=%E6%95%B0%E5%AD%97%E8%AF%97%E6%84%8F
def check(x):
    if x == 1:
        return False
    while x != 1:
        if x & 1:
            return True
        else:
            x //= 2
    return False
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
   if not check(i):
       ans += 1
print(ans)
