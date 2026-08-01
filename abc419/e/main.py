from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.set_int_max_str_digits(10000000)
sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M, L = map(int, input().split())
A = list(map(int, input().split()))

A = [a%M for a in A]

C = [[0]*M for _ in range(L)]

for j in range(M):
    for i in range(L):
        for idx in range(i, N, L):
            C[i][j] += (j - A[idx])%M

dp = [[INF]*M for _ in range(L+1)]
dp[0][0] = 0

for i in range(1, L+1):
    for j in range(M):
        for k in range(M):
            dp[i][j] = min(dp[i][j], dp[i-1][k] + C[i-1][(j - k)%M])

ans = dp[L][0]
print(ans)
