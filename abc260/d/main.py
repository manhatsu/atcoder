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

N, K = map(int, input().split())
P = list(map(int, input().split()))

S = SortedList() # 表向きの一番上のカード
D = dict()
invD = dict()
L = []
ans = [-1]*N

for i, X in enumerate(P):
    idx = bisect_left(S, X)
    if idx == len(S):
        S.add(X)
        M = len(L)
        D[M] = X
        invD[X] = M
        L.append([X])
    else:
        T = S[idx]
        S.discard(T)
        S.add(X)
        M = invD[T]
        D[M] = X
        invD[X] = M
        L[M].append(X)

    if len(L[M]) == K:
        S.discard(X)
        del D[M]
        del invD[X]
        for lx in L[M]:
            ans[lx-1] = i+1

print(*ans)
    
        


