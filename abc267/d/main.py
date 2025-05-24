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

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[MINF]*(M+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(M+1):
        if i < j:
            continue
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j >= 1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + j*A[i-1])

ans = dp[N][M]

print(ans)
    