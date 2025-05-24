from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from re import X
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

Q = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

A = SortedList()

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        A.add(q[1])
    elif q[0] == 2:
        x, k = q[1], q[2]
        idx = A.bisect_right(x)
        if idx - k < 0:
            print(-1)
        else:
            print(A[idx - k])
    else:
        x, k = q[1], q[2]
        idx = A.bisect_left(x)
        if idx + k - 1 >= len(A):
            print(-1)
        else:
            print(A[idx + k - 1])
