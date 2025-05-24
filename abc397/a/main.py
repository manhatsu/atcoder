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

X = float(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

if X >= 38.0:
    print(1)
elif X < 37.5:
    print(3)
else:
    print(2)