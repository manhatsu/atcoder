from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
# from icecream import ic
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    dp[0][0][i][0] = 1

ans = 0
for i in range(1, N+1): # i個目まで見る
    for j in range(N+1): # j個選ぶ
        for k in range(1, N+1): # kで割る
            for l in range(k): # あまり
                dp[i][j][k][l] += dp[i-1][j][k][l]
                dp[i][j][k][l] %= MOD
                if j > 0:
                    dp[i][j][k][l] += dp[i-1][j-1][k][(l-A[i-1])%k]
                    dp[i][j][k][l] %= MOD

for i in range(0, N+1):
    ans += dp[N][i][i][0]
    ans %= MOD
# ic(dp)
print(ans)