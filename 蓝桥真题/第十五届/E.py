# https://www.lanqiao.cn/problems/19719/learning/?page=1&first_category_id=1&name=%E5%90%8A%E5%9D%A0
def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    # 创建一个二维数组来存储最长公共子串的长度
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0  # 记录最长公共子串的长度
    end_pos = 0     # 记录最长公共子串的结束位置

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0

    # 返回最长公共子串
    return s1[end_pos - max_length:end_pos]

# 测试
s1 = "abcdef"
s2 = "zbcdf"
result = longest_common_substring(s1, s2)
print("最长公共子串是:", result)
