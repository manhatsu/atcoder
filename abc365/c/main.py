# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

# 累積和
S = []
s = 0
for a in A:
    s += a
    S.append(s)

# mを1個1個調べているとTLE
'''
i = N-1
m = A[N-1]
L = S[N-1]

if L <= M:
    ans = 'infinite'
else:
    while L > M:
        m -= 1
        while(A[i] > m):
            if i == -1:
                break
            i -= 1
        if i >= 0:
            L = S[i] + m*(N-1-i)
        else:
            L = m*N
    ans = m
'''

# 二分探索で最適なxを探索

def is_ok(x):
    idx = bisect_left(A, x)
    if idx == 0:
        L = x*N
    else:
        L = S[idx-1]+x*(N-idx)
    return M >= L

def bs(ok, ng): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

x = bs(0, A[-1]+1)
if x == A[-1]:
    x = 'infinite'

print(x)