# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N1, N2, M = map(int, input().split())
# A = list(map(int, input().split()))

G = [[] for i in range(N1+N2)]
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

dist1 = [-1]*N1
dist2 = [-1]*(N1+N2)

dist1[0] = 0
Q = deque([0])
while Q:
    q = Q.popleft()
    for lq in G[q]:
        if dist1[lq] >= 0:
            continue
        dist1[lq] = dist1[q]+1
        Q.append(lq)

dist2[N1+N2-1] = 0
Q = deque([N1+N2-1])
while Q:
    q = Q.popleft()
    for lq in G[q]:
        if dist2[lq] >= 0:
            continue
        dist2[lq] = dist2[q]+1
        Q.append(lq)

print(max(dist1)+max(dist2)+1)

