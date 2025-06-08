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

N, L = map(int, input().split())
P = list(map(int, input().split()))

if L % 3 != 0:
    print(0)
    exit()

D = defaultdict(set)

pos = 0
D[pos].add(0)

for i in range(1, N):
    pos += P[i-1]
    D[pos%L].add(i)

ans = 0

for i in range(L//3):
    temp = 1
    for j in range(3):
        temp *= len(D[i+j*L//3])
    ans += temp

print(ans)