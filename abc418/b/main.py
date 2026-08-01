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

S = input()
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

ret = 0.0
for i in range(len(S)-2):
    for j in range(i+3, len(S)+1):
        if (not S[i] == 't') or (not S[j-1] == 't'):
            continue
        count = S[i:j].count('t')
        if count >= 3:
            # ic(i, j, S[i:j], count)
            ret = max(ret, (count-2)/(len(S[i:j])-2))

print(ret)