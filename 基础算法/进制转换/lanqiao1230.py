# https://www.lanqiao.cn/problems/1230/learning/?page=1&first_category_id=1&problem_id=1230
import sys
input = sys.stdin.readline

int_to_char = "0123456789ABCDEF"

char_to_int = {}
for idx, chr in enumerate(int_to_char):
    char_to_int[chr] = idx

t = int(input())

# print(char_to_int)

for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip() # 默认删除首尾的 空格

    # 先把 n 进制转为 十进制
    s = s[::-1]
    ans = 0
    # print(len(s))
    for i in range(len(s)):
        # print(s[i])
        ans = ans + char_to_int[s[i]] * n ** i

    # 再把十进制转为 m 进制
    res = ""
    while ans != 0:
        res += int_to_char[ans % m]
        ans //= m
    res = res[::-1]
    print(res)