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

N, X = map(int, input().split())
# A = list(map(int, input().split()))
S = input()

X = list(str(bin(X))[2:])

for s in S:
    if s == 'U':
        X.pop()
    elif s == 'L':
        X.append('0')
    else:
        X.append('1')

print(int(''.join(X), 2))