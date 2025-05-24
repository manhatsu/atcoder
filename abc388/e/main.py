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

B = A[:N//2][::-1]
C = A[N//2:][::-1]

# print(B, C)

ans = 0

while len(C) > 0:
    if C[-1] >= B[-1]*2:
        B.pop()
        ans += 1
    C.pop()

print(ans)
