# https://www.lanqiao.cn/problems/3382/learning/?page=1&first_category_id=1&problem_id=3382
# 求出 a 的前缀和
from itertools import accumulate
mod = 1000000007

def get_presum(a):
    sum = list(accumulate(a))
    sum = [x % mod for x in sum]
    return sum

# 快速求出区间 a[l]+...+a[r] 之和
def get_sum(sum, l, r):
    if l == 0:
        return sum[r]
    else:
        return (sum[r] - sum[l - 1] + mod) % mod

n, m = map(int, input().split())
a = list(map(int, input().split()))
# 存储 a 数组各个次方的前缀和
sum_list = []
for i in range(1, 6):
    tmp = [x ** i for x in a]
    sum_list.append(get_presum(tmp))

for _ in range(m):
    l, r, k = map(int, input().split())
    print(get_sum(sum_list[k - 1], l - 1, r - 1))
