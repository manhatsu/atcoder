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

S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

A = [0]*(2**10)
A[0] = 1

ans = 0
now = 0
for i in range(len(S)):
    now = now ^ (1 << int(S[i]))
    ans += A[now]
    A[now] += 1

print(ans)

