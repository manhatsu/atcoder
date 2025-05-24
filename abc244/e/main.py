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

N, M, K, S, T, X = map(int, input().split())
S -= 1
T -= 1
X -= 1
G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append(v)
    G[v].append(u)

dp = [[[0]*2 for _ in range(N)] for _ in range(K+1)]
dp[0][S][0] = 1

for k in range(K):
    for v in range(N):
        for lv in G[v]:
            if lv == X:
                dp[k+1][lv][0] += dp[k][v][1]
                dp[k+1][lv][0] %= MOD
                dp[k+1][lv][1] += dp[k][v][0]
                dp[k+1][lv][1] %= MOD
            else:
                dp[k+1][lv][0] += dp[k][v][0]
                dp[k+1][lv][0] %= MOD
                dp[k+1][lv][1] += dp[k][v][1]
                dp[k+1][lv][1] %= MOD

print(dp[K][T][0])