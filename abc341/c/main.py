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

H, W, N = map(int, input().split())
T = input()
F = []
for i in range(H):
    F.append(input())

D = {'L':0, 'R':1, 'U':2, 'D':3}
dh = [0, 0, -1, 1]
dw = [-1, 1, 0, 0]

ans = 0
for h in range(1, H-1):
    for w in range(1, W-1):
        if F[h][w] == '#':
            continue
        nh = h
        nw = w
        ret = True
        for t in T:
            nh += dh[D[t]]
            nw += dw[D[t]]
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                ret = False
                break
            if F[nh][nw] == '#':
                ret = False
                break
        if ret:
            ans += 1

print(ans)