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
from atcoder.dsu import DSU

MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M, Q = map(int, input().split())

Edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    Edges.append((c, a, b, -1)) # from, to, cost, isE if >-1

for i in range(Q):
    x, y, z = map(int, input().split())
    x, y = x-1, y-1
    Edges.append((z, x, y, i))

Edges = sorted(Edges)

U = DSU(N)
yess = set()

for i in range(len(Edges)):
    c, a, b, isE = Edges[i]
    if U.same(a, b):
        continue
    if isE >= 0:
        yess.add(isE)
    else:
        U.merge(a, b)

for i in range(Q):
    print("Yes" if i in yess else "No")

