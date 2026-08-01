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
S = input()
T = input()

D = [[] for _ in range(26)]
for i in range(N):
    D[ord(T[i]) - ord('a')].append(i)


seen = [-1] * 26
for i, d in enumerate(D):
    if len(d) == 0:
        continue
    for idx in d:
        if seen[ord(S[idx]) - ord('a')] == -1:
            seen[ord(S[idx]) - ord('a')] = i
        else:
            if seen[ord(S[idx]) - ord('a')] != i:
                print(-1)
                exit()



