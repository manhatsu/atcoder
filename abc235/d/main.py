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

a, N = map(int, input().split())
# A = list(map(int, input().split()))

A = [INF]*(10**6+1)
A[1] = 0
Q = deque([(1, 0)])

while Q:
    q, r = Q.popleft()

    if q % 10 != 0:
        s = str(q)
        t = s[-1] + s[:-1]
        t = int(t)
        if len(str(t)) <= len(str(N)) and A[t] > r + 1:
            A[t] = r + 1
            Q.append((t, r + 1))

    u = q*a
    if len(str(u)) <= len(str(N)) and A[u] > r + 1:
        A[u] = r + 1
        Q.append((u, r + 1))

if A[N] == INF:
    print(-1)
else:
    print(A[N])