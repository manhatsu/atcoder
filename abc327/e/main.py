# from collections import defaultdict, deque
# from itertools import combinations, permutations
import math
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
P = list(map(int, input().split()))
P = P[::-1]

dp = [[0.0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j-1] + (0.9**(j-1))*P[i-1])

ans = MINF
temp1 = 0
for j in range(1, N+1):
    temp1 += 0.9 ** (j-1)
    temp = dp[N][j] / temp1 - 1200 / math.sqrt(j)
    ans = max(ans, temp)

print(ans)
