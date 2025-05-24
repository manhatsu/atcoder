from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

L, Q = map(int, input().split())
# A = list(map(int, input().split()))

A = SortedList([])

for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        A.add(x)
    else:
        if len(A) == 0:
            print(L)
            continue
        r = A.bisect_left(x)
        if r == 0:
            print(A[0])
            continue
        if r == len(A):
            print(L-A[-1])
            continue
        print(A[r]-A[r-1])
