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

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

cand_edges = []
for i in range(N):
    for j in range(i+1, N):
        cand_edges.append((i, j))

G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    cand_edges.remove((u, v))
    G[u].append(v)
    G[v].append(u)

C = [-1]*N
Q = deque()
Q.append(0)
C[0] = 0
while Q:
    v = Q.popleft()
    for nv in G[v]:
        if C[nv] != -1:
            continue
        C[nv] = 1-C[v]
        Q.append(nv)

toremoves = []
for u, v in cand_edges:
    if C[u] == C[v]:
        toremoves.append((u, v))

for u, v in toremoves:
    cand_edges.remove((u, v))

if len(cand_edges) % 2 == 0:
    print('Second', flush=True)
else:
    print('First', flush=True)
    print(cand_edges[0][0]+1, cand_edges[0][1]+1, flush=True)
    cand_edges.pop(0)

while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    u -= 1
    v -= 1
    if u > v:
        u, v = v, u
    cand_edges.remove((u, v))

    print(cand_edges[0][0]+1, cand_edges[0][1]+1, flush=True)
    cand_edges.pop(0)

exit()

