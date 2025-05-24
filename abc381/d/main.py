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

seen = dict()

ans = 0
left_end = 0
i = 0

# 偶数idx
while i < N-1:
    if A[i] != A[i+1]:
        left_end = i + 2
    else:
        if A[i] in seen:
            left_end = max(left_end, seen[A[i]] + 2)
        seen[A[i]] = i
    ans = max(ans, i+2-left_end)
    i += 2

seen = dict()

# 奇数idx
left_end = 1
i = 1
while i < N-1:
    if A[i] != A[i+1]:
        left_end = i + 2
    else:
        if A[i] in seen:
            left_end = max(left_end, seen[A[i]] + 2)
        seen[A[i]] = i
    ans = max(ans, i+2-left_end)
    i += 2

print(ans)