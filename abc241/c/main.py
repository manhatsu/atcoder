from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from unittest.util import _count_diff_all_purpose
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
F = []
for _ in range(N):
    F.append(input())

def check(i, j):
    if i+5 < N:
        count_h = 0
        for k in range(6):
            if F[i+k][j] == '.':
                count_h += 1
        if count_h <= 2:
            return True
    if j+5 < N:
        count_w = 0
        for l in range(6):
            if F[i][j+l] == '.':
                count_w += 1
        if count_w <= 2:
            return True
    if i+5 < N and j+5 < N:
        count_d = 0
        for m in range(6):
            if F[i+m][j+m] == '.':
                count_d += 1
        if count_d <= 2:
            return True
    if i+5 < N and j-5 >= 0:
        count_d1 = 0
        for n in range(6):
            if F[i+n][j-n] == '.':
                count_d1 += 1
        if count_d1 <= 2:
            return True
    return False

for i in range(N):
    for j in range(N):
        if check(i, j):
            print("Yes")
            exit()
print("No")


