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
S  = [input() for _ in range(N)]

dp = [[0]*2 for _ in range(N+1)] # 0: False, 1: True
dp[0][1] = 1
dp[0][0] = 1

for i in range(N):
    if S[i] == 'AND':
        dp[i+1][1] = dp[i][1]
        dp[i+1][0] = dp[i][0]*2 + dp[i][1]
    else:
        dp[i+1][1] = dp[i][0] + dp[i][1]*2
        dp[i+1][0] = dp[i][0]

print(dp[N][1])