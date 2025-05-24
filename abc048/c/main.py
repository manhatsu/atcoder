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

N, x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
if A[0] > x:
    toadd = A[0]-x
    A[0] = x
    ans += toadd
prev_A = A[0]
for i in range(1, N):
    if prev_A+A[i] > x:
        toadd = prev_A+A[i] - x
        A[i] = x - prev_A
        ans += toadd
    prev_A = A[i]

print(ans)

