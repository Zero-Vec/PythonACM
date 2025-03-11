# from functools import lru_cache
import time
import sys
sys.setrecursionlimit(100000)
dic = {0:1, 1:1}
# @lru_cache(maxsize=None)
def f(x):
    if x in dic.keys():
        return dic[x]
    # if x == 0 or x == 1:
    #     return 1
    dic[x] = (f(x - 1) + f(x - 2)) % 1000000007
    # return f(x - 1) + f(x - 2)
    return dic[x]
n = int(input())
t1 = time.perf_counter()
print(f(n))
t2 = time.perf_counter()
print(t2 - t1)