from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(X): # average
    B = [a-X for a in A]
    S = [0]*(N+1)
    T = [0]*(N+1)

    for i in range(1, N+1):
        S[i] = max(S[i-1], T[i-1])+B[i-1]
        T[i] = S[i-1]

    return max(S[N], T[N]) >= 0

def is_ok1(X): # median
    B = [1 if a >= X else -1 for a in A]
    S = [0]*(N+1)
    T = [0]*(N+1)

    for i in range(1, N+1):
        S[i] = max(S[i-1], T[i-1])+B[i-1]
        T[i] = S[i-1]

    return max(S[N], T[N]) > 0

def bs(ok, ng): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1e-4:
        mid = (ok+ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

def bs1(ok, ng): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok1(mid):
            ok = mid
        else:
            ng = mid
    return ok

ret0 = bs(0, 10**9+1)
ret1 = bs1(0, 10**9+1)

print(ret0)
print(ret1)