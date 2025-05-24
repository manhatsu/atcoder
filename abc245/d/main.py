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

N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]

def solve(X, Z):
    if len(Z) == len(X):
        return Z[0] // X[0], []
    q = Z[0] // X[0]
    if len(X) == 1:
        return q, Z[1:]
    E = Z[1:len(X)]
    F = [x*q for x in X[1:]]
    D = [e - f for e, f in zip(E, F)]
    return q, D+Z[len(X):]

B = []
while len(C) > 0:
    q, C = solve(A, C)
    B.append(q)

print(*B[::-1])

