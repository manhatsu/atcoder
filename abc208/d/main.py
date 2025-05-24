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
F = [[[INF]*(N+1) for i in range(N+1)] for j in range(N+1)]
for i in range(1, N+1):
    for j in range(0, N+1):
        F[i][i][j] = 0

for i in range(M):
    a, b, c = map(int, input().split())
    F[a][b][0] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            F[i][j][k] = min(F[i][j][k-1], F[i][k][k-1]+F[k][j][k-1])

ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if F[i][j][k] == INF:
                continue
            ans += F[i][j][k]

print(ans)    