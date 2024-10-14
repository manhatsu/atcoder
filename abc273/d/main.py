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

H, W, rs, cs = map(int, input().split())
N = int(input())
rs, cs = rs-1, cs-1
dicth = defaultdict(list)
dictw = defaultdict(list)

for i in range(N):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    dicth[r].append(c)
    dictw[c].append(r)

for key in dicth:
    dicth[key].sort()
for key in dictw:
    dictw[key].sort()

nowh, noww = rs, cs
Q = int(input())
for i in range(Q):
    d, l = input().split()
    l = int(l)

    if d == 'L':
        if nowh in dicth:
            adj_wall_idx = bisect_right(dicth[nowh], noww) - 1
            if adj_wall_idx == -1:
                noww = max(0, noww-l)
            else:
                noww = max(dicth[nowh][adj_wall_idx]+1, noww-l)
        else:
            noww = max(0, noww-l)

    elif d == 'R':
        if nowh in dicth:
            adj_wall_idx = bisect_left(dicth[nowh], noww)
            if adj_wall_idx == len(dicth[nowh]):
                noww = min(W-1, noww+l)
            else:
                noww = min(dicth[nowh][adj_wall_idx]-1, noww+l)
        else:
            noww = min(W-1, noww+l)

    elif d == 'U':
        if noww in dictw:
            adj_wall_idx = bisect_right(dictw[noww], nowh) - 1
            if adj_wall_idx == -1:
                nowh = max(0, nowh-l)
            else:
                nowh = max(dictw[noww][adj_wall_idx]+1, nowh-l)
        else:
            nowh = max(0, nowh-l)

    else:
        if noww in dictw:
            adj_wall_idx = bisect_left(dictw[noww], nowh)
            if adj_wall_idx == len(dictw[noww]):
                nowh = min(H-1, nowh+l)
            else:
                nowh = min(dictw[noww][adj_wall_idx]-1, nowh+l)
        else:
            nowh = min(H-1, nowh+l)

    print(nowh+1, noww+1)