n = int(input())
dic = {}
for i in range(n):
    id, x, y = input().split()
    dic[x] = (id, y)
m = int(input())
qur = list(input().split())
for i in range(m):
    print(dic[qur[i]][0], end=' ')
    print(dic[qur[i]][1])
