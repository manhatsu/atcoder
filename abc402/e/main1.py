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
# A = list(map(int, input().split()))

S = []
C = []
P = []
for _ in range(N):
    s, c, p = map(int, input().split())
    S.append(s)
    C.append(c)
    P.append(float(p)/100)

dp = [[0.0]*(X+1) for _ in range(2**N)]

# もらうDP
for x in range(X+1):
    for s in range(2**N):
        for i in range(N):
            xx = x - C[i]
            ss = s | (1 << i)
            if xx < 0 or ss == s:
                continue
            dp[s][x] = max(dp[s][x], P[i]*(dp[ss][xx] + S[i]) + (1-P[i])*dp[s][xx])

print(dp[0][X])