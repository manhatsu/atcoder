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
# from icecream import ic

N, K, Q = map(int, input().split())
# A = list(map(int, input().split()))

S = 0
A = [0]*N
L = SortedList(A)

for _ in range(Q):
    x, y = map(int, input().split())
    y = -y
    x -= 1
    # ic(x, y)
    # ic(A)
    # ic(L)
    prev_y = A[x]
    A[x] = y
    if K == N:
        S -= prev_y
        S += y
        print(-S)
        continue
    prev_yidx = L.bisect_left(prev_y)
    # ic(prev_yidx)
    if prev_yidx < K:
        S -= prev_y
        L.discard(prev_y)
        S += L[K-1]
    else:
        L.discard(prev_y)
    # ic(S)
    # ic(L)
    
    yidx = L.bisect_left(y)
    # ic(yidx)
    if yidx < K:
        S += y
        S -= L[K-1]
        L.add(y)
    else:
        L.add(y)
    
    # ic(S)
    # ic(L)
    print(-S)
