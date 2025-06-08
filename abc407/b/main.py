from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
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

X, Y = map(int, input().split())
# A = list(map(int, input().split()))

a = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i+j >= X or abs(i-j) >= Y:
            a += 1

print(float(a) / 36.0)