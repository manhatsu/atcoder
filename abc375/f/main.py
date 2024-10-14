from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M, Q = map(int, input().split())

dist = [[INF]*N for i in range(N)]
for i in range(N):
    dist[i][i] = 0

edge_list = []
for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edge_list.append((a, b, c))
    dist[a][b] = c
    dist[b][a] = c

querys = []
for i in range(Q):
    q = list(map(int, input().split()))
    querys.append(q)

for i in range(Q):
    l = querys[i]
    if l[0] == 2:
        continue
    a, b, _ = edge_list[l[1]-1]
    dist[a][b] = INF
    dist[b][a] = INF

for k in range(N): 
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

ret = []
for i in range(Q):
    l = querys.pop()
    if l[0] == 2:
        ret.append(dist[l[1]-1][l[2]-1] if dist[l[1]-1][l[2]-1] < INF else -1)
        continue
    a, b, c = edge_list[l[1]-1]
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][a]+dist[b][j]+c, dist[i][b]+dist[a][j]+c)

ret = ret[::-1]
for r in ret:
    print(r)
