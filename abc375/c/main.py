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
G = []
for i in range(N):
    G.append(input())

def getRotatedIdx(i, j, t):
    if t == 0:
        return i, j
    if t == 1:
        return N-1-j, i
    if t == 2:
        return N-1-i, N-1-j
    else:
        return j, N-1-i

F = ['' for i in range(N)]
for i in range(N):
    for j in range(N):
        t = (min(i,j,N-1-i,N-1-j) + 1) % 4
        ri, rj = getRotatedIdx(i, j, t)
        F[i] += G[ri][rj]

for i in range(N):
    print(F[i])