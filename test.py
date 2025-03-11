from functools import lru_cache

@lru_cache(maxsize=None)
def f(x):
    if x == 1:
        return 1
    ans = 1
    for i in range(1, x // 2 + 1):
        ans = ans + f(i)
    return ans

n = int(input())
print(f(n))