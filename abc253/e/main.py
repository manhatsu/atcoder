from collections import defaultdict, deque
from curses.panel import update_panels
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from mimetypes import init
from os import F_OK
from sortedcontainers import SortedSet, SortedDict, SortedList
from atcoder.lazysegtree import LazySegTree
import copy
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M, K = map(int, input().split())

dp = [[0]*(M+1) for _ in range(N)]
for i in range(1, M+1):
    dp[0][i] = 1

for i in range(1, N):
    S = []
    temp = 0
    for j in range(M+1):
        temp += dp[i-1][j]
        temp %= MOD
        S.append(temp)
    for j in range(1, M+1):
        if K == 0: # K=0の時に2回重複して足し算しないようにする
            dp[i][j] = S[M]
            continue
        if j-K >= 1:
            dp[i][j] += S[j-K]%MOD
        if j+K <= M:
            dp[i][j] += (S[M] - S[j+K-1])%MOD
        dp[i][j] %= MOD

ans = sum(dp[N-1]) % MOD

print(ans)


