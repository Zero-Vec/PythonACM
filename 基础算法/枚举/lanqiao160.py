# https://www.lanqiao.cn/problems/160/learning/?page=1&first_category_id=1&tag_relation=intersection&name=%E5%AD%97%E7%AC%A6%E8%AE%A1%E6%95%B0
s = input()
sum1, sum2 = 0, 0
for i in s:
    if i in "aeiou":
        sum1 += 1
    else:
        sum2 += 1
print(sum1)
print(sum2)
