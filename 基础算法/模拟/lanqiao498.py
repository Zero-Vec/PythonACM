# https://www.lanqiao.cn/problems/498/learning/?page=1&first_category_id=1&problem_id=498
import datetime
# print(datetime.datetime.now())
date = input()
y = int(date[0:4])
m = int(date[4:6])
d = int(date[6:])
# print(y)
# print(m)
# print(d)
dd = datetime.date(y,m,d) # 将 y、m、d 转化为日期格式
# print(dd)
tag = True # 输出一次回文日期
for i in range(999999999):
    dd = dd + datetime.timedelta(days=1)
    strdd = str(dd).replace('-','')
    if strdd == strdd[::-1]:
        if tag:
            print(strdd)
            tag = False
        if not tag:
            if strdd[0] == strdd[2] == strdd[5] == strdd[7] and strdd[1] == strdd[3] == strdd[4] == strdd[6]:
                print(strdd)
                break
