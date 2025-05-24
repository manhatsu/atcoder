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
A = list(map(int, input().split()))

dp0 = [[INF]*2 for _ in range(N)]
dp0[0][1] = A[0]

for i in range(1, N):
    dp0[i][0] = min(dp0[i][0], dp0[i-1][1])
    dp0[i][1] = min(dp0[i][1], dp0[i-1][0]+A[i], dp0[i-1][1]+A[i])

dp1 = [[INF]*2 for _ in range(N)]
dp1[0][0] = 0

for i in range(1, N):
    dp1[i][0] = min(dp1[i][0], dp1[i-1][1])
    dp1[i][1] = min(dp1[i][1], dp1[i-1][0]+A[i], dp1[i-1][1]+A[i])

ans = min(dp0[N-1][0], dp0[N-1][1], dp1[N-1][1])

print(ans)