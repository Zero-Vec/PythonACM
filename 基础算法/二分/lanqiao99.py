# https://www.lanqiao.cn/problems/99/learning/?page=1&first_category_id=1&tag_relation=intersection&name=%E5%88%86%E5%B7%A7%E5%85%8B%E5%8A%9B
n, k = map(int, input().split())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

def check(x):
    cnt = 0
    for h, w in a:
        cnt += (h // x) * (w // x)
    return cnt >= k

ans = 1
l, r = 1, 100000

while l <= r:
    mid = (l + r) // 2
    # print(mid)
    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
