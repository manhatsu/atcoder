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

N, Z = map(int, input().split())
G = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

toadd = [0]*N
for i in range(Z):
    p, x = map(int, input().split())
    p = p-1
    toadd[p] += x

seen = [-1]*N
seen[0] = toadd[0]
Q = deque()
Q.append(0)

while Q:
    q = Q.popleft()
    for lq in G[q]:
        if seen[lq] != -1:
            continue
        seen[lq] = seen[q] + toadd[lq]
        Q.append(lq)

print(*seen)


