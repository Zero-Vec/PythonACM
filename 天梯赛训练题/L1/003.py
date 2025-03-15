# s = input()
# dic = {}
# for ch in s:
#     if ch in dic.keys():
#         dic[ch] += 1
#     else:
#         dic[ch] = 1
# # print(dic)
# # 以键的大小从小到大排序
# sorted_dic = sorted(dic.items(), key=lambda x:x[0], reverse=False)
# # print(sorted_dic)
# for i, c in sorted_dic:
#     print(f"{i}:{c}")

s = input()
cnt = [0] * 10
for ch in s:
    num = int(ch)
    cnt[num] += 1
for i in range(10):
    if cnt[i] != 0:
        print(f"{i}:{cnt[i]}")
