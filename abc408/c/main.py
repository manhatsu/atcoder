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

N, M = map(int, input().split())
# A = list(map(int, input().split()))

F = [0]*(N)

for _ in range(M):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    F[l] += 1
    if r+1 <= N-1:
        F[r+1] -= 1

S = []
s = 0
for i in range(N):
    s += F[i]
    S.append(s)

print(min(S))

    

