# https://oj.socoding.cn/contest/problem?id=656&pid=0
def poly_dec(s):
    mp = {'A': 0, 'D': 1, 'F': 2, 'G': 3, 'X': 4}
    ans = []
    i = 0
    while i < len(s) - 1:
        r = mp.get(s[i], 5)
        l = mp.get(s[i + 1], 5)
        ch = chr(r * 5 + l + ord('A'))

        if ch == 'I' and i + 2 < len(s) and s[i + 2] == 'S':
            ans.append('J')
            i += 1
        else:
            if ch <= 'I':
                ans.append(ch)
            else:
                ans.append(chr(ord(ch) + 1))
        i += 2
    return ''.join(ans)

def dec(s, key):
    ans = []
    for i in range(len(s)):
        c = ord(s[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        p = chr((c - k + 26) % 26 + ord('A'))
        ans.append(p)
    return ''.join(ans)

def enc(s, key):
    ans = []
    for i in range(len(s)):
        p = ord(s[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        c = chr((p + k) % 26 + ord('A'))
        ans.append(c)
    return ''.join(ans)


def solve():
    str = input()
    key = input()

    s1 = dec(str, key)
    s2 = enc(str, key)
    # print(s1, s2)
    s1 = poly_dec(s1)
    s2 = poly_dec(s2)

    if s1[0:9] == "IZUNACHAN":
        print(s1[9:])
    else:
        print(s2[9:])


if __name__ == "__main__":
    t = 1
    while t > 0:
        solve()
        t -= 1