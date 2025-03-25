import datetime

a = datetime.date(2025, 3, 25)
print("type(a) =", type(a))
print("a =", a)
print("a.year =", a.year)
print("a.month =", a.month)
print("a.day =", a.day)
# 周几 周一~周日: 0~6
print("a.weekday =", a.weekday())

b = datetime.date(2025, 3, 27)
# 两个日期相减的结果是时间间隔
print(type(b - a))
print(b - a)
