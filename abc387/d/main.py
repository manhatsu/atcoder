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

H, W = map(int, input().split())
F = []
for _ in range(H):
    F.append(input())

sh, sw = -1, -1
gh, gw = -1, -1

for h in range(H):
    for w in range(W):
        if F[h][w] == 'S':
            sh, sw = h, w
        elif F[h][w] == 'G':
            gh, gw = h, w

seen = [[[-1]*2 for w in range(W)] for h in range(H)]

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

Q = deque()
seen[sh][sw][0] = 0
seen[sh][sw][1] = 0
Q.append((sh, sw, 0))
Q.append((sh, sw, 1))

ans = -1
while Q:
    nh, nw, nd = Q.popleft()
    if nh == gh and nw == gw:
        ans = seen[nh][nw][nd]
        break
    nexd = 1-nd
    for i in range(nexd, 4, 2):
        nexh = nh + dh[i]
        nexw = nw + dw[i]
        if nexh < 0 or nexw < 0 or nexh >= H or nexw >= W:
            continue
        if F[nexh][nexw] == '#':
            continue
        if seen[nexh][nexw][nexd] != -1:
            continue
        seen[nexh][nexw][nexd] = seen[nh][nw][nd] + 1
        Q.append((nexh, nexw, nexd))

print(ans)