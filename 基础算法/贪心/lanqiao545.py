# https://www.lanqiao.cn/problems/545/learning/?page=1&first_category_id=1&name=%E8%B0%88%E5%88%A4
import heapq

n = int(input())
a = list(map(int, input().split()))

# print(a)
heapq.heapify(a)
ans = 0
while len(a) >= 2:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    ans += x + y
    heapq.heappush(a, x + y)

print(ans)
