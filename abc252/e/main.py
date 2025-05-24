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

N, M = map(int, input().split())
# A = list(map(int, input().split()))
G = [[] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    G[a].append((c, b, i+1))
    G[b].append((c, a, i+1))

H = []
heapq.heapify(H)
heapq.heappush(H, (0, 0, -1))

dist = [INF]*N
dist[0] = 0

ans_edges = []

while len(H) > 0:
    d, v, e = heapq.heappop(H)
    if dist[v] < d:
        continue
    ans_edges.append(e)
    for c, lv, f in G[v]:
        if dist[lv] > d+c:
            dist[lv] = d+c
            heapq.heappush(H, (dist[lv], lv, f))

ans_edges = sorted(ans_edges)[1:]

print(*ans_edges)