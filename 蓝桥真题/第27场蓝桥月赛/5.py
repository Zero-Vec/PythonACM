from collections import defaultdict
MOD = 10**9 + 7

def solve(N, D, A):

    # 按国家分组，记录每个国家的电脑编号列表
    cou_group = defaultdict(list)
    for i in range(N):
        cou_group[A[i]].append(i + 1)

    dp = [1]  # dp[k] 表示选择 k 台电脑的合法方式数量

    for computers in cou_group.values():
        computers.sort()  # 将电脑编号排序
        n = len(computers)
        # 计算当前国家的合法方式
        # 选择 0 台：1 种方式
        # 选择 1 台：n 种方式
        # 选择 2 台：满足距离不超过 D 的方式
        count_2 = 0
        left = 0
        for right in range(n):
            while computers[right] - computers[left] > D:
                left += 1
            count_2 += right - left
        # 更新 dp
        new_dp = [0] * (len(dp) + 2)
        for k in range(len(dp)):
            new_dp[k] = (new_dp[k] + dp[k]) % MOD  # 不选当前国家的电脑
            new_dp[k + 1] = (new_dp[k + 1] + dp[k] * n) % MOD  # 选 1 台
            new_dp[k + 2] = (new_dp[k + 2] + dp[k] * count_2) % MOD  # 选 2 台
        dp = new_dp

    # 总方式数为 dp[1] + dp[2] + ... + dp[N]
    total = (sum(dp[1:]) % MOD)
    return total

N, D = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, D, A))