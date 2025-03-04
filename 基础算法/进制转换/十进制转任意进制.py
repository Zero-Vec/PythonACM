# 整数部分：除 k 取余法 逆序输出
# 小数部分：乘 K 取整法 顺序输出

# 把十进制的数字转成 k 进制
# 输入：k：int、x：str
# 输出：ans：str 转换成k进制的答案

int_to_char = "0123456789ABCDEF"

def Ten_To_K(k, x):
    ans = ""
    while x != 0:
        ans += int_to_char[x % k]
        x //= k
    return ans[::-1]

k = 2
x = 19
print(Ten_To_K(k, x))
