# https://www.lanqiao.cn/problems/1371/learning/?page=1&first_category_id=1&problem_id=1371
# s = input()
# if s == s[::-1]:
#     print('Y')
# else:
#     print('N')

s = list(input())
l, r = 0, len(s) - 1
tag = 'Y'
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        tag = 'N'
        break
print(tag)