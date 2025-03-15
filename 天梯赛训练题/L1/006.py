import math
n = int(input())
ans, first = 0, 0
for i in range(2, int(math.sqrt(n)) + 3):
    tmp, tag = 1, i
    for j in range(i, int(math.sqrt(n)) + 3):
        tmp *= j
        if n % tmp != 0:
            tag = j
            break
    if tag - i > ans:
        ans = tag - i
        first = i
if first == 0:
    print(1)
    print(n)
else:
    print(ans)
    for i in range(first, first + ans):
        if i == first:
            print(i, end='')
        else:
            print(f"*{i}", end='')
