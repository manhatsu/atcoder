from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from operator import le
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

def calc_slope(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    if dx == 0:
        return(1, 0)
    if dy == 0:
        return(0, 1)
    g = math.gcd(dy, dx)
    dy //= g
    dx //= g
    if dx < 0:
        dy = -dy
        dx = -dx
    return (dy, dx)

N = int(input())
# N, K = map(int, input().split())
P = []
for i in range(N):
    x1, y1 = map(int, input().split())
    P.append((x1, y1))

D = defaultdict(int)
M = defaultdict(int)

for i in range(N-1):
    for j in range(i+1, N):
        if i == j:
            continue
        x1, y1 = P[i]
        x2, y2 = P[j]
        mid = ((x1 + x2) / 2, (y1 + y2) / 2)
        slope = calc_slope(x1, y1, x2, y2)
        # ic(i, j, slope)
        M[mid] += 1
        D[slope] += 1


num_trapezoids = 0
for slope, counts in D.items():
    if counts >= 2:
        num_trapezoids += counts * (counts - 1) // 2

num_parallelograms = 0
for mid, count in M.items():
    if count >= 2:
        num_parallelograms += count * (count - 1) // 2

# ic(num_trapezoids, num_parallelograms)
print(num_trapezoids - num_parallelograms)

