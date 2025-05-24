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
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

if N == 1:
    ans = 2
else:
    dp = [[0]*2 for i in range(N)]
    dp[0][0] = 1
    dp[0][1] = 1

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] * int(A[i] != A[i-1]) % MOD + dp[i-1][1] * int(A[i] != B[i-1]) % MOD
        dp[i][1] = dp[i-1][0] * int(B[i] != A[i-1]) % MOD + dp[i-1][1] * int(B[i] != B[i-1]) % MOD
        dp[i][0] %= MOD
        dp[i][1] %= MOD

    ans = (sum(dp[N-1])%MOD)

print(ans)
