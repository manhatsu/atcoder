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
A = list(map(int, input().split()))

ans = 0

D0 = defaultdict(int)
D1 = defaultdict(int)

for a in A:
    D1[a] += 1

for a in A:
    D1[a] -= 1
    if D1[a] == 0:
        del D1[a]
    D0[a] += 1
    ans = max(ans, len(D0)+len(D1))

print(ans)

