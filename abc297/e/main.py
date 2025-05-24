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

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
ret = []
S  = SortedSet([0])
while len(ret) < K+1:
    temp = S.pop(0)
    ret.append(temp)
    for a in A:
        S.add(temp+a)

print(ret[-1])