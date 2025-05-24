from collections import defaultdict, deque
import copy
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

N, M, K = map(int, input().split())
# A = list(map(int, input().split()))

if N == 1:
    print(min(M, K))
    exit()

S = [0]*(K+1)
for i in range(1, M+1):
    S[i] = 1

for i in range(1, K+1):
    S[i] += S[i-1]
    S[i] %= MOD

# if N > 10:
    # ic.disable()

# ic(S)

for i in range(N-1):
    dp1 = [0]*(K+1)
    for k in range(K+1):
        dp1[k] = S[max(k-1, 0)] - S[max(0, k-M-1)]
        dp1[k] %= MOD
    # ic(dp1)
    S = copy.deepcopy(dp1)
    for k in range(i+2, K+1):
        S[k] += S[k-1]
        S[k] %= MOD

# ic(S)

print(S[K])





