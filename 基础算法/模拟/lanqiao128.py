# https://www.lanqiao.cn/problems/128/learning/?page=1&first_category_id=1&problem_id=128
n = int(input())
mx = 0
def calculate(x):
    global mx
    n_start = x
    while x != 1 and x >= n_start:
        mx = max(mx, x)
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
for i in range(1, n + 1):
    calculate(i)
print(mx)

# 如果运算过程中n小于一开始的n，那就不用求了，因为底下的for循环中已经求过了，
# 比如你求1~5的，在5那里求出一个n=4的结果，那肯定f(4)已经执行过了，有最大值也求完了，就没必要再求一遍了
# 反复求是耽误这个算法效率的核心原因