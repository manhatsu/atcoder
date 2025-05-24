from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from numpy import gradient
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)

sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, X = map(int, input().split())
S = []
C = []
P = []
for _ in range(N):
    s, c, p = map(int, input().split())
    S.append(s)
    C.append(c)
    P.append(p/100)

# ic(S, P)

dp = [[0]*(X+1) for _ in range(2**N)]
for s in range(2**N-1, -1, -1):
    for x in range(X, -1, -1):
        for i in range(N):
            if (s & (1 << i)) or (x + C[i] > X):
                continue
            dp[s][x] = max(dp[s][x], (1-P[i])*dp[s][x+C[i]]+P[i]*(dp[s | (1 << i)][x+C[i]]+S[i]))

print(dp[0][0])