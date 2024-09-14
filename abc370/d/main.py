# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
from sortedcontainers import SortedSet, SortedList, SortedDict
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

H, W, Q = map(int, input().split())

horiz = [SortedSet([i for i in range(W)]) for j in range(H)]
vert = [SortedSet([j for j in range(H)]) for i in range(W)]

for i in range(Q):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    if c in horiz[r]:
        horiz[r].discard(c)
        vert[c].discard(r)
        continue
    l = horiz[r].bisect_left(c)
    if l > 0:
        lv = horiz[r].pop(l-1)
        vert[lv].discard(r) # type: ignore
    l = horiz[r].bisect_left(c)
    if l < len(horiz[r]):
        rv = horiz[r].pop(l)
        vert[rv].discard(r) # type: ignore

    u = vert[c].bisect_left(r)
    if u > 0:
        uh = vert[c].pop(u-1)
        horiz[uh].discard(c)
    u = vert[c].bisect_left(r)
    if u < len(vert[c]):
        dh = vert[c].pop(u)
        horiz[dh].discard(c)       

sum = 0
for h in horiz:
    sum += len(h)

print(sum)