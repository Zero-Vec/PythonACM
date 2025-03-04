# https://www.lanqiao.cn/problems/1331/learning/?page=1&first_category_id=1&problem_id=1331
x = int(input())
ans = 0
for i in range(32):
    if (x >> i) & 1 == 1:
        ans += 1
print(ans)
