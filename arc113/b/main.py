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

A, B, C = map(int, input().split())

a = int(str(A)[-1])

L = [a]
while True:
    a = (a*A)%10
    if a == L[0]:
        break
    L.append(a)

# print(L)
temp = pow(B%len(L), C, len(L))
print(L[temp-1])



