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
Q = deque()
for i in range(N):
    t, x, a = map(int, input().split())
    Q.append((t, x, a))

dp = [[0]*5 for i in range(10**5+1)]
for i in range(1, 10**5+1):
    if Q and Q[0][0] == i:
        _, x, a = Q.popleft()
    else:
        x, a = -1, 0
    for j in range(5):
        if j == x:
            for k in range(max(0, j-1), min(j+2, 5)):
                dp[i][j] = max(dp[i][j], dp[i-1][k]+a)
        else:
            for k in range(max(0, j-1), min(j+2, 5)):
                dp[i][j] = max(dp[i][j], dp[i-1][k])
    for j in range(5):
        if j > i:
            dp[i][j] = 0

# for i in range(6):
    # print(*dp[i])

print(max(dp[10**5]))