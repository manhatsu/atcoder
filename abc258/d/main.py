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
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

S = []
s = 0
for a, b in zip(A, B):
    s += a
    s += b
    S.append(s)

C = []
temp_min = INF
for b in B:
    temp_min = min(temp_min, b)
    C.append(temp_min)

ans = INF
for i in range(N):
    ans = min(ans, S[i]+C[i]*(X-i-1))

print(ans)