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

from atcoder.dsu import DSU

N, M = map(int, input().split())
# A = list(map(int, input().split()))
edges = []
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a-1, b-1))
    G[a-1].append(b-1)
    G[b-1].append(a-1)

U = DSU(N)
for a, b in edges:
    U.merge(a, b)
if U.size(0) != N:
    print('No')
    exit()

for g in G:
    if len(g) != 2:
        print('No')
        exit()

print('Yes')
