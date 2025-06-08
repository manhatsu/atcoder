from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.set_int_max_str_digits(10000000)
sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
B = list(map(int, input().split()))
B = sorted(B)[::-1]
W = list(map(int, input().split()))
W = sorted(W)[::-1]

SB = [0]
sb = 0
for b in B:
    sb += b
    SB.append(sb)

SW = [0]
sw = 0
for w in W:
    if w < 0:
        break
    sw += w
    SW.append(sw)

ans = 0
for i in range(N+1):
    if i >= len(SW):
        ans = max(ans, SB[i]+SW[-1])
    else:
        ans = max(ans, SB[i] + SW[i])

print(ans)
