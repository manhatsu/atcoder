from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.set_int_max_str_digits(10000000)
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

from atcoder.dsu import DSU

N, M = map(int, input().split())
# A = list(map(int, input().split()))
G = [[] for _ in range(N)]
H = []
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)
    H.append((a, b))


ret = True
max_jisuu = max(len(G[i]) for i in range(N))
if max_jisuu > 2:
    ret = False
if ret:
    U = DSU(N)
    for a, b in H:
        if U.same(a, b):
            ret = False
            break
        U.merge(a, b)
print("Yes" if ret else "No")