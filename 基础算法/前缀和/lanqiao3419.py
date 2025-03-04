# https://www.lanqiao.cn/problems/3419/learning/?page=1&first_category_id=1&problem_id=3419
from itertools import accumulate

def get_presum(a):
    sum = list(accumulate(a))
    return sum

def get_sum(sum, l, r):
    if l == 0:
        return sum[r]
    else:
        return sum[r] - sum[l - 1]

s = input()
a = []
for x in s:
    if x == 'L':
        a.append(-1)
    else:
        a.append(1)
sum = get_presum(a)
n = len(a)
mx = 0
for l in range(n):
    for r in range(l, n):
        if get_sum(sum, l, r) == 0:
            mx = max(mx, r - l + 1)
print(mx)