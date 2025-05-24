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

X = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

i = 2
while True:
    X = X // i
    if X == 1:
        print(i)
        break
    i += 1