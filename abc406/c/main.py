from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

L = []
U = []

status = 0 # 0: low, 1: high
for i in range(N-1):
    if status == 0 and A[i+1] > A[i]:
        L.append(i)
        status = 1
    elif status == 1 and A[i+1] < A[i]:
        U.append(i)
        status = 0

if status == 1:
    U.append(N-1)
elif status == 0:
    L.append(N-1)

if len(L) > len(U):
    L.pop()
if len(L) <= 1:
    ans = 0
else:
    ans = 0
    for i in range(len(L)-1):
        ans += (U[i+1] - L[i+1]) * (U[i] - L[i])
        

print(ans)
