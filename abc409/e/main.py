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

N = int(input())
X = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

cost = 0
def dfs(v, p):
    e = X[v]
    global cost
    for u, w in G[v]:
        if u == p:
            continue
        d = dfs(u, v)
        cost += abs(d) * w
        e += d
    # ic(v, e, cost)
    return e

dfs(0, -1)
print(cost)
