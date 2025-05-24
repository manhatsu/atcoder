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

N, M = map(int, input().split())

G = [[] for i in range(N)]
H = [set() for i in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    G[u].append((v, w))
    G[v].append((u, w))
    H[u].add(v)

seen = [0]*N
vals = [0]*N

for i in range(N):
    if seen[i]:
        continue
    seen[i] = 1
    Q = deque([i])

    while Q:
        q = Q.popleft()
        for lq, w in G[q]:
            if seen[lq]:
                continue
            seen[lq] = 1
            if lq in H[q]:
                vals[lq] = vals[q] + w
            else:
                vals[lq] = vals[q] - w
            Q.append(lq)

print(*vals)