def f(n):
    if n <= 1:
        return 1
    ans = n * f(n - 1)
    return ans

print(f(6))
