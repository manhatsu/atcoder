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

N, X = map(int, input().split())

U = []
D = []

maxH = INF
for _ in range(N):
    u, d = map(int, input().split())
    U.append(u)
    D.append(d)
    maxH = min(maxH, u+d)

def isOK(h):
    for i in range(N):
        if i == 0:
            minu = max(0, h-D[i])
            maxu = min(U[i], h)
            continue
        minu = max(minu-X, max(0, h-D[i]))
        maxu = min(maxu+X, min(U[i], h))
        if minu > maxu:
            return False
    return True

def bs(ok, ng):
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok

HH = bs(-1, maxH+1)

ans = 0
for i in range(N):
    ans += U[i]+D[i]-HH

print(ans)



