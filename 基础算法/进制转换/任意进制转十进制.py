# 把 k 进制的数字转成十进制
# 输入：k：int、x：str
# 输出：ans：int

int_to_char = "0123456789ABCDEF"
char_to_int = {}
for idx, chr in enumerate(int_to_char):
    char_to_int[chr] = idx

print(char_to_int)

# (x[0]*k^(n-1) + x[1]*k^(n-2) + ... + x[n-1]*k^0 )
def K_To_Ten(k, x):
    ans = 0
    x = x[::-1]
    # '0-9':0-9 ; 'A'-'F':10-15
    for i in range(len(x)):
        ans = ans + char_to_int[x[i]] * k ** i
    return ans

# k = 8
# x = "3506"
# print(K_To_Ten(k, x))
# 整数小数分开算
