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
X, Y = map(int, input().split())

A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[INF]*(Y+1) for _ in range(X+1)]
dp[0][0] = 0

for i in range(N):
    a = A[i]
    b = B[i]
    temp_dp = [dp[j][:] for j in range(X+1)]
    for x in range(X+1):
        for y in range(Y+1):
            if dp[x][y] == INF:
                continue
            temp_dp[min(X, x+a)][min(Y, y+b)] = min(temp_dp[min(X, x+a)][min(Y, y+b)], dp[x][y]+1)
    dp = temp_dp

if dp[X][Y] == INF:
    print(-1)
else:
    print(dp[X][Y])