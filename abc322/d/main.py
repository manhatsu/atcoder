from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
from copy import deepcopy
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

P = []
for _ in range(3):
    p = [[0]*4 for h in range(4)]
    for h in range(4):
        s = input()
        for w in range(4):
            if s[w] == "#":
                p[h][w] = 1
    P.append(p)

F = [[0]*4 for _ in range(4)]

def rotate(p):
    q = [[0]*4 for _ in range(4)]
    for h in range(4):
        for w in range(4):
            q[w][3-h] = p[h][w]
    return q

def layout(F, p, dh, dw):
    for h in range(4):
        for w in range(4):
            if p[h][w] == 0:
                continue
            hh = h+dh
            ww = w+dw
            if hh < 0 or hh >= 4 or ww < 0 or ww >= 4:
                return False
            if F[hh][ww] == 1:
                return False
            if F[hh][ww] == 0:
                F[hh][ww] = 1
    return True

def dfs(i, F):
    if i == 3:
        ret = 1
        for h in range(4):
            for w in range(4):
                ret &= F[h][w]
        if ret:
            return True
        else:
            return False
    for dh in range(-3, 4):
        for dw in range(-3, 4):
            p = P[i]
            G = deepcopy(F)
            if layout(G, p, dh, dw): 
                ret = dfs(i+1, G)
                if ret:
                    return True
    return False

ans = False
for i in range(4):
    for j in range(4):
        if dfs(0, F):
            ans = True
            break
        P[1] = rotate(P[1])
    if ans:
        break
    P[0] = rotate(P[0])

print("Yes" if ans else "No")

