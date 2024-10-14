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

N, x, y = map(int, input().split())
A = list(map(int, input().split()))

if N == 2:
    if A[0] == x:
        isOKH = 1
    else:
        isOKH = 0
    if (A[1] == y) or (-A[1] == y):
        ifOKV = 1
    else:
        isOKV = 0

else:
    H = A[2::2]
    V = A[1::2]

    ofs = 10**4
    dph = [[0]*(2*(10**4)+1) for i in range(len(H)+1)]
    dph[0][A[0]+ofs] = 1
    dpv = [[0]*(2*(10**4)+1) for i in range(len(V)+1)]
    dpv[0][ofs] = 1

    for i in range(1, len(H)+1):
        for j in range(-10**4, 10**4+1):
            if j - H[i-1] + ofs >= 0:
                dph[i][j+ofs] |= dph[i-1][j-H[i-1]+ofs]
            if j + H[i-1] + ofs <= 2*10**4:
                dph[i][j+ofs] |= dph[i-1][j+H[i-1]+ofs]
    isOKH = dph[-1][x+ofs]

    for i in range(1, len(V)+1):
        for j in range(-10**4, 10**4+1):
            if j - V[i-1] + ofs >= 0:
                dpv[i][j+ofs] |= dpv[i-1][j-V[i-1]+ofs]
            if j + V[i-1] + ofs <= 2*10**4:
                dpv[i][j+ofs] |= dpv[i-1][j+V[i-1]+ofs]
    isOKV = dpv[-1][y+ofs]

print('Yes' if (isOKH and isOKV) else 'No')
