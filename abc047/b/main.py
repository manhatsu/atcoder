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

W, H, N = map(int, input().split())

F = [[0]*W for _ in range(H)]

for _ in range(N):
    x, y, a = map(int, input().split())
    # x, y = x-1, y-1
    if a == 1:
        if x == 0:
            continue
        for h in range(H):
            for w in range(x):
                F[h][w] = 1
    elif a == 2:
        if x == W:
            continue
        for h in range(H):
            for w in range(x, W):
                F[h][w] = 1
    elif a == 3:
        if y == 0:
            continue
        for h in range(y):
            for w in range(W):
                F[h][w] = 1
    elif a == 4:
        if y == H:
            continue
        for h in range(y, H):
            for w in range(W):
                F[h][w] = 1

ans = 0
for h in range(H):
    for w in range(W):
        ans += F[h][w] == 0

print(ans)