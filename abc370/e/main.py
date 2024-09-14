# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 998244353

dp = [[0]*4 for _ in range(N+1)]

for i in range(N):
    if A[i] != K:
        dp[i+1][0] = 0
        dp[i+1][1] = (dp[i][0] + dp[i][1]) % MOD
        dp[i+1][2] = 0
        dp[i+1][3] = dp[i][2] + dp[i][3]
    else:
        if i == 0:
            dp[i+1][0] = 1
            dp[i+1][1] = 0
        else:
            dp[i+1][0] = (dp[i][0] + dp[i][1]) % MOD
            dp[i+1][1] = 0
            dp[i+1][2] = ((2**i) % MOD - dp[i+1][0] % MOD) % MOD
            dp[i+1][3] = 0

print((dp[N][2] + dp[N][3]) % MOD)