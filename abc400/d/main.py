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
# A = list(map(int, input().split()))
S = []
for _ in range(H):
    S.append(input())
A, B, C, D = map(int, input().split())
A, B, C, D = A-1, B-1, C-1, D-1

Q = deque()
Q.append((A, B, 0))

seen = [[0] * W for _ in range(H)]
seen[A][B] = 1
while Q:
    h, w, c = Q.popleft()
    if h == C and w == D:
        print(c)
        exit()
    for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nh, nw = h + dh, w + dw
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if seen[nh][nw]:
            continue
        seen[nh][nw] = 1
        if S[nh][nw] == '#':
            Q.append((nh, nw, c+1))
            if 0 <= nh+dh < H and 0 <= nw+dw < W:
                Q.append((nh+dh, nw+dw, c+1))
        else:
            Q.appendleft((nh, nw, c))
    
