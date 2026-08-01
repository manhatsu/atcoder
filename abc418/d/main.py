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

N = int(input())
T = input()
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

is_good = [0]*N
is_good[0] = int(T[0])
for i in range(1, N):
    is_good[i] = 1 - is_good[i-1]^int(T[i])

# ic(is_good)

S = []
s = 0
for i in range(N):
    s += is_good[i]
    S.append(s)

ans = 0
for j in range(1, N+1):
    # ic(j, is_good[j-1], S[j-1])
    if is_good[j-1] == 0:
        ans += (j-1-S[j-1])
    else:
        ans += S[j-1]

print(ans)
