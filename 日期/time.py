import time

# start_time = time.time()
# print(f'开始时间：{start_time}')
#
# time.sleep(3)
#
# end_time = time.time()
# print(f'结束时间：{end_time}')
#
# print("运行时间：{:.0f}".format(end_time - start_time))

t = time.localtime()
print("type(t) =", type(t))
print("t =", t)
print("年份 =", t.tm_year) # 四位数
print("月份 =", t.tm_mon) # 1-12
print("日期 =", t.tm_mday) # 1-31
print("小时 =", t.tm_hour) # 0-23
print("分钟 =", t.tm_min) # 0-59
print("秒 =", t.tm_sec) # 0-59
print("一周的第几日 =", t.tm_wday) # 0-6,0是周一
print("一年的第几日 =", t.tm_yday) # 1-366
print("夏令时标识 =", t.tm_isdst) # 夏令时标识

# 获取本地时间
t = time.localtime()
# 本地时间转换成一个字符串
str_t = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("str_t =", str_t)
print("type(str_t) =", type(str_t))
# 将一个字符串转换成时间类型
str_t = time.strptime(str_t, "%Y-%m-%d %H:%M:%S")
print("str_t =", str_t)
print("type(str_t) =", type(str_t))
