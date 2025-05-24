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

appetites = []
for i in range(N):
    x, y = map(int, input().split())
    appetites.append((x, y))

dp = [[0]*2 for i in range(N+1)]

for i in range(N):
    x, y = appetites[i]
    if x == 0:
        dp[i+1][0] = max(max(dp[i][0]+y, dp[i][1]+y), dp[i][0])
        dp[i+1][1] = dp[i][1]
    else:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = max(dp[i][0]+y, dp[i][1])

print(max(dp[N]))