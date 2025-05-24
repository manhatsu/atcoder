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

N, M, K = map(int, input().split())


G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

D = [-1]*N

for i in range(K):
    p, h = map(int, input().split())
    p -= 1
    D[p] = h

Q = [(-d, i) for i, d in enumerate(D) if d != -1] # heapは小さい順に出てくるので-1をかけて格納する

heapq.heapify(Q)

while len(Q) > 0:
    d, q = heapq.heappop(Q)
    d = -d
    if d < D[q]:
        continue
    for lq in G[q]:
        if d-1 > D[lq]:
            D[lq] = d-1
            heapq.heappush(Q, (-(d-1), lq))

ans = [i+1 for i in range(N) if D[i] > -1]

print(len(ans))
print(*ans)