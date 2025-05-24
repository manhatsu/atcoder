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
# from icecream import # ic

N = int(input())
C = list(map(int, input().split()))
C = [c-1 for c in C]
C = C+C
# N, K = map(int, input().split())
X = list(map(int, input().split()))

dp = [[INF]*(2*N) for _ in range(2*N)]

for j in range(2*N-1, -1, -1):
    prev_seen = defaultdict(lambda: -1)
    for i in range(j, 2*N):
        if j == i:
            dp[j][i] = 1 + X[C[j]]
            prev_seen[C[j]] = i
            continue
        if prev_seen[C[i]] != -1:
            if C[i] == C[i-1]:
                if dp[j][i-1] != INF:
                    dp[j][i] = min(dp[j][i], dp[j][i-1]+1)
            else:
                if dp[j][i-1] != INF:
                    dp[j][i] = min(dp[j][i], dp[j][i-1]+1+X[C[i]])
                if dp[j][prev_seen[C[i]]] != INF and dp[prev_seen[C[i]]+1][i-1] != INF:
                    dp[j][i] = min(dp[j][i], dp[j][prev_seen[C[i]]]+dp[prev_seen[C[i]]+1][i-1] + (i - prev_seen[C[i]]))
        else:
            if dp[j][i-1] != INF:
                dp[j][i] = min(dp[j][i], dp[j][i-1]+1+X[C[i]])
        # if C[i] == 2:
            # # ic(j, i, prev_seen[C[i]], dp[j][i], dp[j][i-1], dp[j][prev_seen[C[i]]], dp[prev_seen[C[i]]+1][i-1])
        
        prev_seen[C[i]] = i

ans = INF
for i in range(N):
    ans = min(ans, dp[i][i+N-1])

print(ans)
