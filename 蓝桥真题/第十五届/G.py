# https://www.lanqiao.cn/problems/19720/learning/?page=1&first_category_id=1&name=%E6%99%BA%E5%8A%9B%E6%B5%8B%E8%AF%95
import os
import sys

def make_array(length,val):
    return [val for _ in range(length)]
def make_2d_array(rows,cols,val):
    return [[val for _ in range(cols)] for _ in range(rows)]
def make_3d_array(d1,d2,d3,val):
    return [[[val for _ in range(d3)] for _ in range(d2)] for _ in range(d1)]

def read_int():
    return int(input())
def read_ints():
    return [int(i) for i in input().split()]

mod = int(1e9) + 7

n,m,T = read_ints()
dup_rows = []
prod_rows = make_2d_array(n,18,0)
rrfl = make_array(n,0)
last = -1

rr = read_ints()

for idx,it in enumerate(sorted(list(enumerate(rr)),key=lambda x:x[1])):
    # rows: [(idx,val),...]
    if it[1] != last:
        last = it[1]
        dup_rows.append([last,1])
    else:
        dup_rows[-1][1] += 1
    rrfl[it[0]] = len(dup_rows) - 1
for i,val in enumerate(dup_rows):
    prod_rows[i][0] = val[1]
for i in range(1,18):
    for j in range(0,len(dup_rows) - (1 << i) + 1):
        prod_rows[j][i] = prod_rows[j][i - 1] * prod_rows[j + (1 << (i - 1))][i - 1] % mod

dup_cols = []
crfl = make_array(m,0)
prod_cols = make_2d_array(m,18,0)
last = -1

cc = read_ints()

for idx,it in enumerate(sorted(list(enumerate(cc)),key=lambda x:x[1])):
    if it[1] != last:
        last = it[1]
        dup_cols.append([last,1])
    else:
        dup_cols[-1][1] += 1
    crfl[it[0]] = len(dup_cols) - 1
for i,val in enumerate(dup_cols):
    prod_cols[i][0] = val[1]
for i in range(1,18):
    for j in range(0,len(dup_cols) - (1 << i) + 1):
        prod_cols[j][i] = prod_cols[j][i - 1] * prod_cols[j + (1 << (i - 1))][i - 1] % mod

def cal_prod(begin,count,arr):
    ans = 1;base = 0
    while count > 0:
        if count & 1:
            ans = ans * arr[begin][base] % mod
            begin += 1 << base
        count >>= 1
        base += 1
    return ans


fact = make_array(n + m + 5, 1)
for i in range(2, n + m + 5):
    fact[i] = fact[i - 1] * i % mod
invs = make_array(n + m + 5, 1)


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(b, k=mod):
    gcd, x, _ = extended_gcd(b, k)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {b} mod {k}")
    return x % k


for i in range(n + m + 5):
    invs[i] = mod_inverse(fact[i])


def C(tol, choice):
    return fact[tol] * invs[tol - choice] * invs[choice] % mod


for ct in range(T):
    ans = 1
    r1, c1, r2, c2 = [i - 1 for i in read_ints()]

    # if ct == 11:
    # print("debug: r1,r2,c1,c2:",r1,r2,c1,c2)
    # print("debug: len(rr),len(cc):",len(rr),len(cc))
    # print("debug:",rrfl[r1],rrfl[r2],crfl[c1],crfl[c2])
    # print("debug:",rr[r1],rr[r2],cc[c1],cc[c2])
    # exit(0)

    if rrfl[r1] >= rrfl[r2]:
        if r1 != r2:
            print(0)
            continue
    else:
        ans *= cal_prod(rrfl[r1] + 1, rrfl[r2] - rrfl[r1] - 1, prod_rows)
    if crfl[c1] >= crfl[c2]:
        if c1 != c2:
            print(0)
            continue
    else:
        ans *= cal_prod(crfl[c1] + 1, crfl[c2] - crfl[c1] - 1, prod_cols)
    print(ans * C(rrfl[r2] + crfl[c2] - rrfl[r1] - crfl[c1], crfl[c2] - crfl[c1]) % mod)
