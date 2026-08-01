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

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)

S = []
s = 0
for i in range(N):
    s += A[i]
    S.append(s)

for _ in range(Q):
    b = int(input())
    idx = bisect_left(A, b)
    if idx == N:
        ans = -1
    elif idx == 0:
        ans = (b-1) * (N - idx) + 1
    else:
        ans = S[idx-1] + (b-1) * (N - idx) + 1

    print(ans)

