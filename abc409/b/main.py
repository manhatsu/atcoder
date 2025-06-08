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
A = list(map(int, input().split()))
A = sorted(A)[::-1]

ans = [0] * 101

for a in A:
    for i in range(min(a+1, 101)):
        ans[i] += 1

ret = 0
for i in range(len(ans)):
    if ans[i] >= i:
        ret = max(ret, i)

print(ret)

