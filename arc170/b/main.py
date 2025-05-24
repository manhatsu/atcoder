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

G = [[-1]*11 for _ in range(N)]

for i in range(1, N):
    for j in range(1, 11):
        if A[i-1] == j:
            G[i][j] = i-1
        else:
            G[i][j] = G[i-1][j]

ans = 0
maxi = -1

for k in range(2, N):
    for jval in range(1, 11):
        ival = 2*jval - A[k]
        if ival < 1 or ival > 10:
            continue
        j = G[k][jval]
        if j <= 0:
            continue
        i = G[j][ival]
        maxi = max(maxi, i)
    ans += maxi+1

print(ans)
