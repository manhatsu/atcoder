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

N, M = map(int, input().split())

dh = [2, 1, -1, -2, -2, -1, 1, 2]
dw = [1, 2, 2, 1, -1, -2, -2, -1]

ng_set = set()
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    ng_set.add((a, b))
    for i in range(8):
        na = a+dh[i]
        nb = b+dw[i]
        if (na < 0) or (na >= N) or (nb < 0) or (nb >= N):
            continue
        ng_set.add((na, nb))

ngs = len(ng_set)
print(N**2-ngs)