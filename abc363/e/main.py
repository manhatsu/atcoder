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

H, W, Y = map(int, input().split())

G = []
for i in range(H):
    G.append(list(map(int, input().split())))
seen = [[-1]*W for i in range(H)]

Q = [[] for i in range(10**5+1)]

for h in range(H):
    for w in range(W):
        if h == 0 or w == 0 or h == H-1 or w == W-1:
            seen[h][w] = 1
            Q[G[h][w]].append((h, w))

# print(Q[:Y+1])

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
area = H*W
for i in range(1, Y+1):
    if len(Q[i]) == 0:
        print(area)
        continue
    for h, w in Q[i]:
        for j in range(4):
            nh = h+dh[j]
            nw = w+dw[j]
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            if seen[nh][nw] != -1:
                continue
            seen[nh][nw] = 1
            if G[nh][nw] <= i:
                Q[i].append((nh, nw))
            else:
                Q[G[nh][nw]].append((nh, nw))
    area -= len(Q[i])
    print(area)