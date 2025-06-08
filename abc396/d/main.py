from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
# sys.set_int_max_str_digits(10000000)
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

G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    G[u].append((v, w))
    G[v].append((u, w))

ans = INF
def dfs(v, val):
    global ans
    if v == N-1:
        ans = min(ans, val)
        return 
    for u, w in G[v]:
        if seen[u] == 0:
            seen[u] = 1
            dfs(u, val ^ w)
            seen[u] = 0

seen = [0] * N
seen[0] = 1
dfs(0, 0)
print(ans)
