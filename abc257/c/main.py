from calendar import c
from collections import defaultdict, deque
from email.policy import default
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# from icecream import ic
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
S = input()
S = list(S)
S = [int(s) for s in S]
# N, K = map(int, input().split())
W = list(map(int, input().split()))
W, S = zip(*sorted(zip(W, S)))

# ic(W)
# ic(S)

c0 = 0
a0 = 0
c1 = 0
a1 = 0

for i in range(N):
    if S[i] == 0:
        c1 += 1
    else:
        a1 += 1

ans = c0+a1

idx = 0
for i in range(N):
    if S[i] == 0:
        c0 += 1
        c1 -= 1
    else:
        a0 += 1
        a1 -= 1
    if i == N-1 or W[i] != W[i+1]:
        ans = max(ans, c0+a1)

print(ans)
