from calendar import c
from collections import defaultdict, deque
from functools import lru_cache
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

X = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

@lru_cache
def F(x):
    if x <= 4:
        return x
    else:
        a = x // 2
        b = x - a
        return F(a)*F(b)%MOD


print(F(X))