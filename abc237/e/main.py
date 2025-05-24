from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from multiprocessing import heap
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
import heapq
try:
    from icecream import ic
except ImportError:
    # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# 負の辺があるのでそのままダイクストラは使えない
# 楽しさW = H[start] - H[goal] - Cの形になる。Cは上り坂H[v]-H[u]の総和であり、Cを最小化すれば良い。

N, M = map(int, input().split())
H = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    if H[u] > H[v]:
        u, v = v, u # H[u] <= H[v]
    G[u].append((v, H[v] - H[u]))
    G[v].append((u, 0))

dist = [INF]*N
dist[0] = 0

Q = []
heapq.heapify(Q)
heapq.heappush(Q, (0, 0)) # (dist, node)

while Q:
    d, u = heapq.heappop(Q)
    if dist[u] < d:
        continue
    for v, w in G[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(Q, (dist[v], v))

ans = 0
for i in range(N):
    ans = max(ans, -dist[i] + H[0] - H[i])

print(ans)
