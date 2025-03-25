# https://www.lanqiao.cn/problems/889/learning/?page=1&first_category_id=1&problem_id=889
n, m = map(int, input().split())
e = []
for i in range(m):
    u, v, c = map(int, input().split())
    e.append([c, u, v])
e.sort()
pre = [i for i in range(n + 1)]
def root(x):
    if pre[x] == x:
        return x
    else:
        pre[x] = root(pre[x])
        return pre[x]
ans = 0
for w, u, v in e:
    u_root = root(u)
    v_root = root(v)
    if u_root == v_root:
        continue
    else:
        pre[u_root] = v_root
        ans = max(ans, w)
print(n - 1, ans)
