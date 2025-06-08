from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
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


def solve(N, S):
    Q = deque()
    prev = S[0]
    count = 1
    for s in S[1:]:
        if s != prev:
            Q.append((prev, count))
            prev = s
            count = 1
        else:
            count += 1
            continue
    Q.append((prev, count))

    dp = [[[INF]*2 for _ in range(2)] for _ in range(len(Q)+1)] # dp[i][j][k]: 最後がjで終わり、1からなる区間がk個
    dp[0][0][0] = 0
    for i in range(1, len(Q)+1):
        v, c = Q.popleft()
        if v == 0:
            dp[i][1][1] = min(dp[i][1][1], dp[i-1][0][0] + c, dp[i-1][1][1] + c)
            dp[i][0][1] = min(dp[i][0][1], dp[i-1][0][1], dp[i-1][1][1])
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][1][0] = INF
        else:
            dp[i][1][1] = min(dp[i][1][1], dp[i-1][1][1], dp[i-1][0][0])
            dp[i][0][1] = min(dp[i][0][1], dp[i-1][0][1] + c, dp[i-1][1][1]+c)
            dp[i][0][0] = min(dp[i][0][0], dp[i-1][0][0] + c)
            dp[i][1][0] = INF

    ans = INF
    for j in range(2):
        for k in range(2):
            ans = min(ans, dp[i][j][k])
    return ans
        


T = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

for _ in range(T):
    N = int(input())
    S = input()
    S = [int(s) for s in S]
    ans = solve(N, S)
    print(ans)