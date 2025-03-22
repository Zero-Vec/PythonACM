# https://www.acwing.com/problem/content/1211/

# python 过 80% cpp 可 AC

from itertools import permutations

def solve(N):
    digits = "123456789"
    count = 0

    # 遍历所有排列
    for p in permutations(digits):
        s = ''.join(p)  # 将排列转换为字符串
        # 枚举 A 和 B 的分割点
        for i in range(1, len(s)):  # A 至少 1 位
            A = int(s[:i])
            if A >= N:  # 剪枝：如果 A 已经大于 N，跳过
                break
            for j in range(i + 1, len(s)):  # B 至少 1 位
                B = int(s[i:j])
                C = int(s[j:])
                if C != 0 and B % C == 0 and A + B // C == N:
                    count += 1
    return count

N = int(input())
ans = solve(N)
print(ans)
