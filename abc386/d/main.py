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

Q = []

for i in range(M):
    h, w, c = input().split()
    h, w = int(h)-1, int(w)-1
    Q.append((h, w, c))

ret = True
Q = sorted(Q)
min_white_idx = N
for _, w, c in Q:
    if c == 'B':
        if w >= min_white_idx:
            ret = False
            break
    else:
        min_white_idx = min(w, min_white_idx)

print('Yes' if ret else 'No')