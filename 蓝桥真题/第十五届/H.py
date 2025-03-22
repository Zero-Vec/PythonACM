# https://www.lanqiao.cn/problems/19721/learning/?page=1&first_category_id=1&name=%E6%9C%80%E5%A4%A7%E5%BC%82%E6%88%96%E7%BB%93%E7%82%B9

# 第一发暴力：通过50%
n = int(input())
w = list(map(int, input().split()))
a = list(map(int, input().split()))
fa = [-1] * (n + 1)
# son = [[] for _ in range(n + 1)]
for i in range(n):
    if a[i] != -1:
        fa[i] = a[i]
        # son[a[i]].append(i)
# for i in range(n):
#     print(i, fa[i], son[i])
ans = 0
for i in range(n):
    for j in range(n):
        if j != i and fa[i] != j and fa[j] != i:
            ans = max(ans, w[i] ^ w[j])
print(ans)

"""
class TreeNode():
    def __init__(self):
        self.children = [None,None]
        self.num = False


class Tree():
    def __init__(self,max_bit = 32):
        self.root = TreeNode()
        self.max_bit = max_bit

    def insert(self,num):
        node = self.root
        for i in range(self.max_bit-1,-1,-1):
            b = (num>>i)&1
            if node.children[b] is None:
                node.children[b] = TreeNode()
            node = node.children[b]
        node.num = num

    def query(self,num):
        node = self.root
        for i in range(self.max_bit-1,-1,-1):
            opposite_bit = ~(num>>i)&1
            if  node.children[opposite_bit] is None:
                 b = ~opposite_bit
            else:
                 b = opposite_bit
            node = node.children[b]
        return num^node.num

N = int(input())
nums = list(map(int,input().split()))
fa = list(map(int,input().split()))
tree = Tree()
for i in nums:
    tree.insert(i)

ans = 0
for i in nums:
    ans = max(ans, tree.query(i))

print(ans)
"""
