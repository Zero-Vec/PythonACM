# https://www.lanqiao.cn/problems/152/learning/?page=1&first_category_id=1&tag_relation=intersection&name=%E5%8F%8D%E5%80%8D%E6%95%B0
import math
n = int(input())
a, b, c = map(int, input().split())
# ans = 0
# for i in range(1, n + 1):
#     if i % a != 0 and i % b != 0 and i % c != 0:
#         ans += 1
# print(ans)

def lcm(x, y):
    return x * y // math.gcd(x, y)
# 容斥定理：
# 1 ~ n 中 a 的倍数有 n // a 个
# 1 ~ n 中 b 的倍数有 n // b 个
# 1 ~ n 中 ab 的倍数有 n // lcm(a, b) 个
# 1 ~ n 中 a 或者 b 的倍数有 n // a + n // b - n // lcm(a, b) 个
print(n - (n // a + n // b + n // c - n // lcm(a, b) - n // lcm(c, b) - n // lcm(a, c) + n // lcm(lcm(a, b), c)))
