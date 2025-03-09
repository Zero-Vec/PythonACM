# https://www.lanqiao.cn/problems/2942/learning/?page=1&first_category_id=1&problem_id=2942

def check(x, group):
    for i in group:
        if i % x == 0 or x % i == 0:
            return False
    return True

def dfs(depth):
    global ans
    if ans <= len(Groups):
        return
    if depth == n:
        ans = min(ans, len(Groups))
        return
    # 枚举当前人放在哪一组
    for group in Groups:
        if check(a[depth], group):
            group.append(a[depth])
            dfs(depth + 1)
            group.pop()
    # 单独开一组
    Groups.append([a[depth]])
    dfs(depth + 1)
    Groups.pop()

    return

n = int(input())
a = list(map(int, input().split()))
ans = n
Groups = []     # [[], [], []]
dfs(0)
print(ans)