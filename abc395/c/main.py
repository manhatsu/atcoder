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

ans = INF

last_idx = [-1] * (10**6+1)

for i, a in enumerate(A):
    if last_idx[a] != -1:
        ans = min(ans, i - last_idx[a] + 1)
    last_idx[a] = i

print(ans if ans != INF else -1)