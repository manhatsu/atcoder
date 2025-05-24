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

H, W, K = map(int, input().split())
F = []
for i in range(H):
    F.append(input())

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

ans = 0

def dfs(h, w, k):
    global ans
    if k == K:
        ans += 1
        return
    for i in range(4):
        nh = h+dh[i]
        nw = w+dw[i]
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if F[nh][nw] == '#':
            continue
        if seen[nh][nw]:
            continue
        seen[nh][nw] = 1
        dfs(nh, nw, k+1)
        seen[nh][nw] = 0
    
    return
    
for h in range(H):
    for w in range(W):
        if F[h][w] == '#':
            continue
        seen = [[0]*W for h in range(H)]
        seen[h][w] = 1
        dfs(h, w, 0)

print(ans)
