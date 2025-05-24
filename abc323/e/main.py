# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")
# from icecream import ic

N, X = map(int, input().split())
T = list(map(int, input().split()))

dp = [0]*(X+1)
dp[0] = pow(N, -1, MOD)
for i in range(1, X+1):
    for j in range(N):
        if i - T[j] >= 0:
            dp[i] += dp[i-T[j]]*pow(N, -1, MOD)
            dp[i] %= MOD

ans = sum(dp[-T[0]:]) % MOD
print(ans)

a = [1]