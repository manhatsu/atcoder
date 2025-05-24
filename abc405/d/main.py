from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from re import S
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
import copy
sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

H, W = map(int, input().split())

Q = deque()
seen = [[INF] * W for _ in range(H)]

F = []
for i in range(H):
    f = input()
    for j in range(W):
        if f[j] == 'E':
            Q.append((0, i, j))
            seen[i][j] = 0
    F.append(f)

G = copy.deepcopy(F)
for i in range(H):
    G[i] = list(G[i])

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]
arrows = ['>', 'v', '<', '^']

while Q:
    d, h, w = Q.popleft()
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0 <= nh < H and 0 <= nw < W and F[nh][nw] == '.' and seen[nh][nw] > d + 1:
            nd = d + 1
            seen[nh][nw] = nd
            if h == nh:
                if w < nw:
                    G[nh][nw] = '<'
                else:
                    G[nh][nw] = '>'
            else:
                if h < nh:
                    G[nh][nw] = '^'
                else:
                    G[nh][nw] = 'v'
            Q.append((nd, nh, nw))

for i in range(H):
    G[i] = ''.join(G[i])
for i in range(H):
    print(G[i])