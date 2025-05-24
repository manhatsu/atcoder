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

N, A, B, C = map(int, input().split())
D = []

for i in range(N):
    D.append(list(map(int, input().split())))

# print(D)

dist = [INF]*N
dist[0] = 0
pq = []
heapq.heapify(pq)
heapq.heappush(pq, (0, 0))

while len(pq) > 0:
    c, v = heapq.heappop(pq)
    if c > dist[v]:
        continue
    for lv, lc in enumerate(D[v]):
        if dist[lv] > dist[v] + lc*A:
            dist[lv] = dist[v] + lc*A
            heapq.heappush(pq, (dist[lv], lv))

dist1 = [INF]*N
dist1[N-1] = 0
pq1 = []
heapq.heapify(pq1)
heapq.heappush(pq1, (0, N-1))

while len(pq1) > 0:
    c, v = heapq.heappop(pq1)
    if c > dist1[v]:
        continue
    for lv, lc in enumerate(D[v]):
        if dist1[lv] > dist1[v] + lc*B + C:
            dist1[lv] = dist1[v] + lc*B + C
            heapq.heappush(pq1, (dist1[lv], lv))

ans = min([dist[i]+dist1[i] for i in range(N)])
print(ans)