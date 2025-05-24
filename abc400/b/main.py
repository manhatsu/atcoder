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

N, M = map(int, input().split())
# A = list(map(int, input().split()))

X = 0
for i in range(M+1):
    if pow(N, i) > 10**9:
        X = -1
        break
    X += pow(N, i)
    if X > 10**9:
        X = -1
        break

print(X if X != -1 else 'inf')