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

X, A, D, N = map(int, input().split())
# A = list(map(int, input().split()))

if D == 0:
    print(X-A)

else:
    if X-A / D < 0:
        print(X)
    elif X-A / D >= N:
        print(X-(A+N*D))
    else:
        n0 = (X-A) // D
        n1 = n0 + 1
        print(min(X-(A+n0*D), A+n1*D-X))