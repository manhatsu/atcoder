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
X = list(map(int, input().split()))

D = dict()
for _ in range(M):
    c, y = map(int, input().split())
    D[c] = y

dp = [[-1]*(N+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(i+1):
        if dp[i][j] == -1:
            continue
        if j+1 in D:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i]+D[j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i])
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])

# print(*dp, sep="\n")

ans = 0
for i in range(N+1):
    ans = max(ans, dp[N][i])
print(ans)

