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

dp = [[[INF]*501 for i in range(501)] for j in range(101)]
dp[0][0][0] = 0

sum = 0
for i in range(1, N+1):
    a, b = map(int, input().split())
    a -= 1
    sum += b
    for j in range(501):
        for k in range(501):
            if a == 0:
                if j+b <= 500:
                    dp[i][j+b][k] = min(dp[i][j+b][k], dp[i-1][j][k])
                if k+b <= 500:
                    dp[i][j][k+b] = min(dp[i][j][k+b], dp[i-1][j][k]+1)
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k]+1)
            elif a == 1:
                if j+b <= 500:
                    dp[i][j+b][k] = min(dp[i][j+b][k], dp[i-1][j][k]+1)
                if k+b <= 500:
                    dp[i][j][k+b] = min(dp[i][j][k+b], dp[i-1][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k]+1)
            else:
                if j+b <= 500:
                    dp[i][j+b][k] = min(dp[i][j+b][k], dp[i-1][j][k]+1)
                if k+b <= 500:
                    dp[i][j][k+b] = min(dp[i][j][k+b], dp[i-1][j][k]+1)
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])

if sum % 3 != 0:
    ret = INF
else:
    ret = dp[N][sum//3][sum//3]               
print(ret if ret < INF else -1)