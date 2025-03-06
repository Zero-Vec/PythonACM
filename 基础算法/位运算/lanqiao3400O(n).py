# https://www.lanqiao.cn/problems/3400/learning/?page=1&first_category_id=1&problem_id=3400

# 因数个数为偶数 -> 非平方数  正难则反：找平方数
# 前缀异或和
# pre_xor[r] ^ pre_xor[l-1] = [l,r] 的异或结果 x

# 其实应该还有个 O(n) 思路
# pre_xor[r] = x ^ pre_xor[l-1] x是平方数，枚举平方数，看看 r 左边有多少个满足该等式

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 构造前缀异或和数组
pre_xor = [0] * n
pre_xor[0] = a[0]
for i in range(1, n):
    pre_xor[i] = pre_xor[i - 1] ^ a[i]

ans = 0
# 先求出平方数的个数，200 个以内，枚举平方数，由于0的因子数是奇数，所以可将0也视作平方数，从0开始遍历
for i in range(200):
    x = i * i
    # 用字典维护 pre_xor 数组中每个数出现的次数
    dic = {0:1}
    """
    从首项开始进行前缀异或和时，若某项恰为平方数
    可视为该项异或0的结果为平方数，则该项与x的异或结果为0
    则该项满足条件，ans 应该 + 1，故初始时应该设定 dic[0] = 1
    """
    # 枚举 r
    for r in range(n):
        # 检查每次字典中满足条件的数的个数
        ans += dic.get(pre_xor[r] ^ x, 0)
        # 把该项添加到字典中去
        dic[pre_xor[r]] = dic.get(pre_xor[r], 0) + 1
ans = n * (n + 1) // 2 - ans
print(ans)
