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

R = []
C = []
N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

max_r = max(R)
min_r = min(R)
max_c = max(C)
min_c = min(C)

point_r = int((max_r + min_r) / 2 + 0.5)
point_c = int((max_c + min_c) / 2 + 0.5)

ans_r = max(abs(max_r - point_r), abs(min_r - point_r))
ans_c = max(abs(max_c - point_c), abs(min_c - point_c))

print(max(ans_r, ans_c))

# sum_r = sum(R)
# sum_c = sum(C)

# point_r_small = int(sum_r / N + 0.5)
# point_c_small = int(sum_c / N + 0.5)
# point_r_large = point_r_small + 1
# point_c_large = point_c_small + 1

# ans_r_small = 0
# ans_c_small = 0
# ans_r_large = 0
# ans_c_large = 0
# for i in range(N):
#     ans_r_small = max(abs(R[i] - point_r_small), ans_r_small)
#     ans_c_small = max(abs(C[i] - point_c_small), ans_c_small)
#     ans_r_large = max(abs(R[i] - point_r_large), ans_r_large)
#     ans_c_large = max(abs(C[i] - point_c_large), ans_c_large)



