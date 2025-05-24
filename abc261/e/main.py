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

N, C = map(int, input().split())
# A = list(map(int, input().split()))

dp = [[[0]*2 for _ in range(30)] for _ in range(N+1)]

for i in range(30):
    dp[0][i][1] = 1

for i in range(1, N+1):
    t, a = map(int, input().split())
    for j in range(30):
        for k in range(2):
            if t == 1:
                dp[i][j][k] = dp[i-1][j][k] & (a >> j & 1)
            elif t == 2:
                dp[i][j][k] = dp[i-1][j][k] | (a >> j & 1)
            else:
                dp[i][j][k] = dp[i-1][j][k] ^ (a >> j & 1)

x = C
nex = 0
for i in range(1, N+1):
    for j in range(30):
        nex += dp[i][j][x >> j & 1] << j
    x = nex
    print(x)
    nex = 0


