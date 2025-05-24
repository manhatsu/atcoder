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

H, W, N, h, w = map(int, input().split())

F = []
for i in range(H):
    F.append(list(map(int, input().split())))

def add(S, x):
    if x in S:
        S[x] += 1
    else:
        S[x] = 1

def delete(S, x):
    if S[x] == 1:
        del S[x]
    else:
        S[x] -= 1

D = dict()
for i in range(H):
    for j in range(W):
        add(D, F[i][j])

E = []

ans = [[0]*(W-w+1) for _ in range(H-h+1)]

for hh in range(h):
    for ww in range(w):
        delete(D, F[hh][ww])
ans[0][0] = len(D)
E.append(D.copy())

for i in range(1, H-h+1):
    for j in range(w):
        add(D, F[i-1][j])
        delete(D, F[i+h-1][j])
    ans[i][0] = len(D)
    E.append(D.copy())

for i in range(H-h+1):
    U = E[i].copy()
    for j in range(1, W-w+1):
        for k in range(h):
            add(U, F[i+k][j-1])
            delete(U, F[i+k][j+w-1])
        ans[i][j] = len(U)
            
for i in range(H-h+1):
    print(*ans[i])

