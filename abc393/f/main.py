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

N, Q = map(int, input().split())
A = list(map(int, input().split()))

QQ = [[] for i in range(N)]
for i in range(Q):
    r, x = map(int, input().split())
    r -= 1
    QQ[r].append((x, i))

dp = [INF]*(N+1)
dp[0] = 0
ans = [0] * Q

for i in range(N):
    lidx = bisect_left(dp, A[i])
    dp[lidx] = A[i]
    for x, idx in QQ[i]:
        ans[idx] = bisect_right(dp, x) - 1

for a in ans:
    print(a)





