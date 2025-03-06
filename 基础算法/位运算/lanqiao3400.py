# https://www.lanqiao.cn/problems/3400/learning/?page=1&first_category_id=1&problem_id=3400

# 因数个数为偶数 -> 非平方数  正难则反：找平方数
# 前缀异或和
# pre_xor[r] ^ pre_xor[l-1] = [l,r] 的异或结果 x

# 其实应该还有个 O(n) 思路
# pre_xor[r] = x ^ pre_xor[l-1] x是平方数，枚举平方数，看看 r 左边有多少个满足该等式

import math
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

pre_xor = [a[0]]
for i in range(1, n):
    pre_xor.append(pre_xor[i - 1] ^ a[i])
# print(pre_xor)
ans = 0
for l in range(n):
    for r in range(l, n):
        if l == 0:
            tmp = pre_xor[r]
        else:
            tmp = pre_xor[l - 1] ^ pre_xor[r]
        if int(math.sqrt(tmp)) * int(math.sqrt(tmp)) != tmp:
            ans += 1
# ans = n * (n + 1) // 2 - ans
print(ans)
