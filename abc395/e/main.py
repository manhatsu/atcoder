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

N, M, X = map(int, input().split())

G = [[] for _ in range(N)]
INVG = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    INVG[v].append(u)

dist = [[INF]*2 for _ in range(N)]

pq = []
heapq.heapify(pq)
heapq.heappush(pq, (0, 0, 0))
dist[0][0] = 0

while pq:
    c, v, state = heapq.heappop(pq)
    if dist[v][state] < c:
        continue
    if state == 0:
        for lv in G[v]:
            if dist[lv][state] > c+1:
                dist[lv][state] = c+1
                heapq.heappush(pq, (c+1, lv, state))
    else:
        for lv in INVG[v]:
            if dist[lv][state] > c+1:
                dist[lv][state] = c+1
                heapq.heappush(pq, (c+1, lv, state))
    
    if dist[v][1-state] > c+X:
        dist[v][1-state] = c+X
        heapq.heappush(pq, (c+X, v, 1-state))

ans = min(dist[N-1])
print(ans)