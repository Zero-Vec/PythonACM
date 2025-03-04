# https://www.lanqiao.cn/problems/364/learning/?page=1&first_category_id=1&tag_relation=intersection&name=%E8%B7%B3%E7%9F%B3%E5%A4%B4
# 合法判断：假设最短跳跃距离为 x，需移除的石头数量是否 <= M
# 移除的石头数量越多，最短跳跃距离越大
L, N, M = map(int, input().split())
D = []
for i in range(N):
    D.append(int(input()))

def check(x):
    cnt = 0
    # 用 last_id 记录上一个石头的位置
    last_id = 0
    for i in range(N + 1):
        if D[i] - last_id >= x:
            last_id = D[i]
        else:
            cnt += 1

    return cnt <= M

l, r = 1, L
ans = -1
D.append(L)
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)

