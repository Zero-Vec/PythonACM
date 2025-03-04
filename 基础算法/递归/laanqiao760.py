# https://www.lanqiao.cn/problems/760/learning/?page=1&first_category_id=1&problem_id=760
def f(n):
    if n == 1:
        return 1
    ans = 1
    for i in range(1, n // 2 + 1):
        ans = ans + f(i)
    return ans

n = int(input())
print(f(n))
