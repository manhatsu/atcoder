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

T = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

def solve(N, K):
    B = bin(N)[2:]
    dp = [[[0]*2 for i in range(62)] for j in range(62)]
    total = [[[0]*2 for i in range(62)] for j in range(62)]
    dp[0][0][0] = 1
    total[0][0][0] = 0

    for i in range(60):
        c = int(B[i]) if i < len(B) else 0
        for j in range(61):
            for k in range(2):
                for l in range(2): # next bit
                    if k == 0 and c < l:
                        continue
                    nk = 1 if l < c else k
                    dp[i+1][j+l][nk] += dp[i][j][k]
                    dp[i+1][j+l][nk] %= MOD
                    total[i+1][j+l][nk] += (total[i][j][k]*2+ dp[i][j][k]*l) % MOD
                    total[i+1][j+l][nk] %= MOD

    ans = (total[len(B)][K][0] + total[len(B)][K][1]) % MOD
    return ans

for _ in range(T):
    N, K = map(int, input().split())
    ans = solve(N, K)
    print(ans)