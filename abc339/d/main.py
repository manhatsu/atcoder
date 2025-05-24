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
F = []

p0h, p0w = -1, -1
p1h, p1w = -1, -1
for h in range(N):
    F.append(input())
    for w in range(N):
        if F[h][w] == 'P':
            if p0h == -1:
                p0h, p0w = h, w
            else:
                p1h, p1w = h, w

dist = [[[[INF]*N for _ in range(N)] for _ in range(N)] for _ in range(N)]
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
Q = deque()
dist[p0h][p0w][p1h][p1w] = 0
Q.append((p0h, p0w, p1h, p1w, 0))

ans = INF
while Q:
    n0h, n0w, n1h, n1w, v = Q.popleft()
    for i in range(4):
        nn0h = n0h + dh[i]
        nn0w = n0w + dw[i]
        nn1h = n1h + dh[i]
        nn1w = n1w + dw[i]
        flag0 = (nn0h >= 0 and nn0h < N and nn0w >= 0 and nn0w < N and F[nn0h][nn0w] != '#')
        flag1 = (nn1h >= 0 and nn1h < N and nn1w >= 0 and nn1w < N and F[nn1h][nn1w] != '#')
        if not flag0 and not flag1:
            continue
        if not flag0 and flag1:
            nn0h = n0h
            nn0w = n0w
        elif flag0 and not flag1:
            nn1h = n1h
            nn1w = n1w
        if dist[nn0h][nn0w][nn1h][nn1w] != INF:
            continue
        dist[nn0h][nn0w][nn1h][nn1w] = v+1
        Q.append((nn0h, nn0w, nn1h, nn1w, v+1))
        continue
        
for h in range(N):
    for w in range(N):
        if dist[h][w][h][w] == INF:
            continue
        ans = min(ans, dist[h][w][h][w])

print(ans if ans != INF else -1)

