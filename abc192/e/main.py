from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
import heapq

sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M, X, Y = map(int, input().split())
X, Y = X-1, Y-1
G = [[] for _ in range(N)]

if M > 0:
    for _ in range(M):
        A, B, T, K = map(int, input().split())
        G[A-1].append((B-1, T, K))
        G[B-1].append((A-1, T, K))

dist = [INF]*N
dist[X] = 0
Q = []
heapq.heapify(Q)
heapq.heappush(Q, (0, X))

while Q:
    d, v = heapq.heappop(Q)
    if dist[v] < d:
        continue
    for lv, t, k in G[v]:
        towait = 0
        if d%k != 0:
            towait = k-d%k
        if dist[lv] > d+t+towait:
            dist[lv] = d+t+towait
            heapq.heappush(Q, (dist[lv], lv))

print(dist[Y] if dist[Y] != INF else -1)
