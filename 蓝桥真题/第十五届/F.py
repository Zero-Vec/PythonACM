# https://www.lanqiao.cn/problems/19722/learning/?page=1&first_category_id=1&name=%E7%A0%8D%E6%9F%B4
def get_primes(n):
    isprime = [True for _ in range(n + 1)]
    isprime[0] = isprime[1] = False
    result = []
    for i in range(2, n + 1):
        if isprime[i]:
            result.append(i)
            for j in range(2 * i, n + 1, i):
                isprime[j] = False
    return result

# ans = get_primes(100)
# print(ans)
T = int(input())
a = []
mx = 0
for _ in range(T):
    a.append(int(input()))
    mx = max(mx, a[-1])
primes = get_primes(mx)
dp = [0] * (mx + 1)
for i in range(mx + 1):
    if dp[i] == 0:
        for p in primes:
            if p + i > mx:
                break
            dp[i + p] = 1
for i in a:
    print(dp[i])
