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

N = int(input())
# N, K = map(int, input().split())
kukan = []
for i in range(N):
    l, r = map(int, input().split())
    kukan.append((l, r))
kukan = sorted(kukan, key=lambda x: x[1])

S = []
E = []

for l, r in kukan:
    if len(S) == 0:
        S.append(l)
        E.append(r)
        continue
    if l > E[-1]:
        S.append(l)
        E.append(r)
        continue
    k = bisect_left(E, l)
    while len(S) > k+1:
        S.pop()
        E.pop()
    lk = S.pop()
    rk = E.pop()
    S.append(min(lk, l))
    E.append(r)

for s, e in zip(S, E):
    print(s, e)
