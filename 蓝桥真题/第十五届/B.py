# https://www.lanqiao.cn/problems/19700/learning/?page=1&first_category_id=1&name=%E5%8F%AC%E5%94%A4
# def A(x):
#     ans, res = 0, 1
#     for i in range(1, x + 1):
#         ans += i
#         res *= i
#     return ans - res

# cnt = 0
# for i in range(1, 2001):
#     if A(i) % 100 == 0:
#         # cnt += 1
#         print(i, end=' ')
# print(cnt)
# 2024041331404202
a = 2024041331404200
b = a // 200
# c = b * 200
# print(c)
ans = b * 4 + 2
print(ans)
