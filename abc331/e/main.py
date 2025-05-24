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

N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B = [(b, i) for i, b in enumerate(B)]
B = sorted(B, key = lambda x: x[0])[::-1]

C = set()

if L > 0:
    for i in range(L):
        c, d = map(int, input().split())
        C.add((c-1, d-1))

ans = 0
for i, a in enumerate(A):
    j = 0
    while j < M and (i, B[j][1]) in C:
        j += 1
    if j == M:
        continue
    if a + B[j][0] > ans:
        ans = a + B[j][0]

print(ans)