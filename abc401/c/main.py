from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 10 ** 9 # 998244353
INF = float("inf")
MINF = -float("inf")

N, K = map(int, input().split())
# A = list(map(int, input().split()))

A = [0] * (N + 1)
S = [0] * (N + 1)
A[0] = 1
S[0] = 1

for i in range(1, N+1):
    if i < K:
        A[i] = 1
        S[i] = S[i-1] + A[i]
        S[i] %= MOD
        continue
    if i == K:
        A[i] = S[i-1]
        S[i] = S[i-1] + A[i]
        S[i] %= MOD
        continue
    A[i] = S[i-1] - S[i-K-1]
    A[i] %= MOD
    S[i] = S[i-1] + A[i]
    S[i] %= MOD

print(A[N] % MOD)