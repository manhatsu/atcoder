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

N, M = map(int, input().split())
A = list(map(int, input().split()))
D = [0] * (M+1)
for i in range(N):
    D[A[i]] += 1

ans = 0
ret = False
while True:
    for i in range(1, M+1):
        if D[i] == 0:
            ret = True
            break
    if ret:
        break
    ans += 1
    v = A.pop()
    D[v] -= 1

print(ans)