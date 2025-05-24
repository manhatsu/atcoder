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

H, W, N = map(int, input().split())
# A = list(map(int, input().split()))

x_dict = defaultdict(set)
y_dict = defaultdict(set)

for i in range(N):
    x, y = map(int, input().split())
    x_dict[x].add(y)
    y_dict[y].add(x)
Q = int(input())

for _ in range(Q):
    z, w = map(int, input().split())
    if z == 1:
        print(len(x_dict[w]))
        for val in x_dict[w]:
            y_dict[val].remove(w)
        del x_dict[w]
    else:
        print(len(y_dict[w]))
        for val in y_dict[w]:
            x_dict[val].remove(w)
        del y_dict[w]
 
