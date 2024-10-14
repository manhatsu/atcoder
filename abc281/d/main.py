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

N, K, D = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)[::-1]
B = [a%D for a in A]

dp = [[[-1]*D for i in range(N+1)] for j in range(N+1)]
dp[0][0][0] = 0
for i in range(1, N+1):
    for k in range(0, i+1):
        for j in range(D):
            if dp[i-1][k][j] != -1:
                dp[i][k][j] = dp[i-1][k][j]
            if k > 0:
                if dp[i-1][k-1][(j-B[i-1])%D] != -1:
                    dp[i][k][j] = max(dp[i][k][j], dp[i-1][k-1][(j-B[i-1])%D] + A[i-1])

# print(*dp)

print(dp[N][K][0])