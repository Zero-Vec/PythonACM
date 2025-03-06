# https://www.lanqiao.cn/problems/3691/learning/?page=1&first_category_id=1&problem_id=3691

# 1 2 3 4 5
# 001 010 011 100 101
# 预处理出按位的数组，算贡献 ans += (1<<i) & (pre[r] - pre[l - 1])
# (pre[r] - pre[l - 1]) > 1 即可
# [1,0,1,0,1]
# [0,1,1,0,0]
# [0,0,0,1,1]

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

mp = []
# 预处理各个位的数组
for i in range(31):
    tmp = []
    for e in a:
        tmp.append((e >> i) & 1)
    # 前缀和优化
    tmp = [0] + tmp
    l = len(tmp)
    for j in range(1, l):
        tmp[j] += tmp[j - 1]
    mp.append(tmp)

# print(mp)
for _ in range(q):
    l, r = map(int, input().split())
    ans = 0
    for i in range(31):
        now_or = mp[i][r] - mp[i][l - 1]
        if now_or > 0:
            ans += (1 << i)
    print(ans)
