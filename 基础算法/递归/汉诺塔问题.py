# n个盘子从 A 挪到 C,利用中间的B
def Move(n, A, B, C):
    if n == 0:
        return
    # 1.将 n - 1 个盘子从 A 挪到 B
    Move(n - 1, A, C, B)

    # 2.将第 n 个盘子从 A 挪到 C
    print(f"{A}->{C}")
    # 3.将 n - 1 个盘子从 B 挪到 C
    Move(n - 1, B, A, C)

Move(3, 'A', 'B', 'C')