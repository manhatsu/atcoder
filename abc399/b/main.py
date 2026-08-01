from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from multiprocessing import heap
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

N = int(input())
# N, K = map(int, input().split())
P = list(map(int, input().split()))

H = []
heapq.heapify(H)

for i, p in enumerate(P):
    heapq.heappush(H, (-p, i))

r = 1
count = 0
ret = [-1]*N

x, i = heapq.heappop(H)
ret[i] = r
count += 1
while H:
    y, j = heapq.heappop(H)
    if x == y:
        ret[j] = r
        count += 1
    else:
        r += count
        count = 1
        ret[j] = r
        x = y

print(*ret, sep="\n")
    

