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

N, M = map(int, input().split())
S = []

for i in range(N):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    S.append((l, r))

S = sorted(S, key=lambda x: x[1])

ans = 0
idx = 0
D = [0]*M
for l, r in S:
    while idx <= l:
        D[idx] = r-idx
        idx += 1

while idx < M:
    D[idx] = M-idx
    idx += 1

ans = 0
for d in D:
    ans += d

print(ans)