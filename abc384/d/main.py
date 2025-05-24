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

N, S = map(int, input().split())
A = list(map(int, input().split()))

suma = sum(A)

S %= suma

A = A+A

l = 0
r = 0
temp = 0
ans = False
while r < 2*N:
    while temp < S:
        if r >= 2*N:
            break
        temp += A[r]
        r += 1
    if temp == S:
        ans = True
        break
    temp -= A[l]
    l += 1
    if temp == S:
        ans = True
        break

print('Yes' if ans else 'No')