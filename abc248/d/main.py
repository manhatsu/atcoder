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

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

D = [SortedList() for _ in range(N+1)]

for i, a in enumerate(A):
    D[a].add(i)

Q = int(input())
for _ in range(Q):
    l, r, x = map(int, input().split())
    l, r = l-1, r-1

    lidx = D[x].bisect_left(l)
    ridx = D[x].bisect_right(r)
    print(ridx - lidx)

