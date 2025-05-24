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

N, X = map(int, input().split())
V1 = []
V2 = []
V3 = []

for _ in range(N):
    v, a, c = map(int, input().split())
    if v == 1:
        V1.append((a, c))
    elif v == 2:
        V2.append((a, c))
    else:
        V3.append((a, c))

dp1 = [[0]*(X+1) for _ in range(len(V1)+1)]
dp2 = [[0]*(X+1) for _ in range(len(V2)+1)]
dp3 = [[0]*(X+1) for _ in range(len(V3)+1)]

for i in range(len(V1)):
    for j in range(X+1):
        a, c = V1[i]
        dp1[i+1][j] = max(dp1[i+1][j], dp1[i][j])
        if j+c <= X:
            dp1[i+1][j+c] = max(dp1[i+1][j+c], dp1[i][j]+a)

for i in range(len(V2)):
    for j in range(X+1):
        a, c = V2[i]
        dp2[i+1][j] = max(dp2[i+1][j], dp2[i][j])
        if j+c <= X:
            dp2[i+1][j+c] = max(dp2[i+1][j+c], dp2[i][j]+a)

for i in range(len(V3)):
    for j in range(X+1):
        a, c = V3[i]
        dp3[i+1][j] = max(dp3[i+1][j], dp3[i][j])
        if j+c <= X:
            dp3[i+1][j+c] = max(dp3[i+1][j+c], dp3[i][j]+a)

ans = 0
for i in range(X+1):
    for j in range(X+1-i):
        min_w = min(dp1[-1][i], dp2[-1][j], dp3[-1][X-i-j])
        ans = max(ans, min_w)

print(ans)

