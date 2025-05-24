from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import heapq
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

H, W, X = map(int, input().split())
P, Q = map(int, input().split())
P, Q = P-1, Q-1
F = []
for h in range(H):
    F.append(list(map(int, input().split())))

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

seen = [[0]*W for h in range(H)]
seen[P][Q] = 1
takahashi = F[P][Q]

R = []
for i in range(4):
    nh = P + dh[i]
    nw = Q + dw[i]
    if nh < 0 or nw < 0 or nh >= H or nw >= W:
        continue
    if seen[nh][nw]:
        continue
    seen[nh][nw] = 1
    R.append((F[nh][nw], nh, nw))

heapq.heapify(R)

while len(R) > 0:
    v, nowh, noww = heapq.heappop(R)
    if v * X < takahashi:
        takahashi += v
        for i in range(4):
            nh = nowh + dh[i]
            nw = noww + dw[i]
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if seen[nh][nw]:
                continue
            seen[nh][nw] = 1
            heapq.heappush(R, (F[nh][nw], nh, nw))
    else:
        break
print(takahashi)