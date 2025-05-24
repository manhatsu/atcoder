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
# = list(map(int, input().split()))

D = dict()

for _ in range(M):
    a, b = map(int, input().split())
    k = (a+b)%N
    if k not in D:
        D[k] = 1
    else:
        D[k] += 1

ans = M * (M-1) // 2
for key, val in D.items():
    ans -= val * (val - 1) // 2
print(ans)

