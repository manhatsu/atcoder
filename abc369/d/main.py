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

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0]*2 for i in range(N+1)]
dp[0][0] = 0
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = A[0]

if N == 1:
    ans = A[0]
else:
    for i in range(1, N):
        dp[i+1][0] = max(dp[i][0], dp[i][1] + 2*A[i])
        dp[i+1][1] = max(dp[i][1], dp[i][0]+A[i])
    ans = max(dp[N][0], dp[N][1])

print(ans)

