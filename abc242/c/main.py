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
# A = list(map(int, input().split()))

dp = [[0]*9 for _ in range(N)]
for i in range(9):
    dp[0][i] = 1
for i in range(1, N):
    for j in range(9):
        if j - 1 >= 0:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= MOD
        if j + 1 < 9:
            dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= MOD
        dp[i][j] += dp[i-1][j]
        dp[i][j] %= MOD

print(sum(dp[N-1]) % MOD)
