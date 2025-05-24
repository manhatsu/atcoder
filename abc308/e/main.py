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
S = input()

M = [[] for i in range(3)]
X = [[] for i in range(3)]

for i, s in enumerate(S):
    if s == 'M':
        M[A[i]].append(i)
    elif s == 'X':
        X[A[i]].append(i)

rg4 = set([0, 1, 2, 3])

ans = 0
for i, s in enumerate(S):
    if s != 'E':
        continue
    can_m_count = []
    can_x_count = []
    for j in range(3):
        can_m_count.append(bisect_left(M[j], i))
        can_x_count.append(len(X[j]) - bisect_left(X[j], i))

    for j in range(3):
        for k in range(3):
            if can_m_count[j] == 0 or can_x_count[k] == 0:
                continue
            mex_set = (rg4 - set([j, k, A[i]]))
            mex = min(mex_set)
            ans += can_m_count[j]*can_x_count[k]*mex

print(ans)









