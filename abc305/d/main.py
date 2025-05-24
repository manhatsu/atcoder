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

U = A[0::2]
D = A[1::2]

S = [0]
temp = 0
for i in range(N//2):
    temp += U[i+1]-D[i]
    S.append(temp)

def getSleepTime(m):
    if m <= D[0]:
        return 0
    idx = bisect_left(U, m)
    if m > D[idx-1]:
        return S[idx] - (U[idx]-m)
    else:
        return S[idx-1]
    
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    R = getSleepTime(r)
    L = getSleepTime(l)
    print(R-L)
