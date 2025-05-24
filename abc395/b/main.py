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
# A = list(map(int, input().split()))

F = [['#']*N for _ in range(N)]

for i in range(N//2+1):
    for j in range(i, N-i):
        for k in range(i, N-i):
            if i % 2 == 0:
                F[j][k] = '#'
            else:
                F[j][k] = '.'

for i in range(N):
    print("".join(F[i]))
