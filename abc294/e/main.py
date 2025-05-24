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

L, N1, N2 = map(int, input().split())

U = []
D = []
for _ in range(N1):
    v, l = map(int, input().split())
    U.append((v, l))

for _ in range(N2):
    v, l = map(int, input().split())
    D.append((v, l))

idx1 = 0
idx2 = 0
cur1 = 0
cur2 = 0
ans = 0

while idx1 < N1 and idx2 < N2:
    if U[idx1][0] == D[idx2][0]:
        ans += min(cur1+U[idx1][1], cur2+D[idx2][1]) - max(cur1, cur2)
    if cur1+U[idx1][1] < cur2+D[idx2][1]:
        cur1 += U[idx1][1]
        idx1 += 1
    else:
        cur2 += D[idx2][1]
        idx2 += 1

print(ans)
        
        