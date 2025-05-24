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

N, M, sx, sy = map(int, input().split())

xD = dict()
yD = dict()

xL  = []
yL = []

for i in range(N):
    x, y = map(int, input().split())
    if x not in xD:
        xD[x] = len(xL)
        xL.append(SortedList([y]))
    else:
        xL[xD[x]].add(y)
    if y not in yD:
        yD[y] = len(yL)
        yL.append(SortedList([x]))
    else:
        yL[yD[y]].add(x)

nx, ny = sx, sy

ans = 0
for _ in range(M):
    d, c = input().split()
    c = int(c)

    if d == 'U':
        if nx in xD:
            T = xL[xD[nx]]
            _l = T.bisect_right(ny)
            _r = T.bisect_right(ny+c)
            if _l < _r:
                todelY = T[_l:_r]
                ans += len(todelY)
                for todel in todelY:
                    xL[xD[nx]].remove(todel)
                    if len(xL[xD[nx]]) == 0:
                        del xD[nx]
                    yL[yD[todel]].remove(nx)
                    if len(yL[yD[todel]]) == 0:
                        del yD[todel]
        
        ny += c
    
    elif d == 'D':
        if nx in xD:
            T = xL[xD[nx]]
            _l = T.bisect_left(ny-c)
            _r = T.bisect_left(ny)
            if _l < _r:
                todelY = T[_l:_r]
                ans += len(todelY)
                for todel in todelY:
                    xL[xD[nx]].remove(todel)
                    if len(xL[xD[nx]]) == 0:
                        del xD[nx]
                    yL[yD[todel]].remove(nx)
                    if len(yL[yD[todel]]) == 0:
                        del yD[todel]

        ny -= c

    elif d == 'R':
        if ny in yD:
            T = yL[yD[ny]]
            _l = T.bisect_right(nx)
            _r = T.bisect_right(nx+c)
            if _l < _r:
                todelX = T[_l:_r]
                ans += len(todelX)
                for todel in todelX:
                    yL[yD[ny]].remove(todel)
                    if len(yL[yD[ny]]) == 0:
                        del yD[ny]
                    xL[xD[todel]].remove(ny)
                    if len(xL[xD[todel]]) == 0:
                        del xD[todel]         
        
        nx += c

    elif d == 'L':
        if ny in yD:
            T = yL[yD[ny]]
            _l = T.bisect_left(nx-c)
            _r = T.bisect_left(nx)
            if _l < _r:
                todelX = T[_l:_r]
                ans += len(todelX)
                for todel in todelX:
                    yL[yD[ny]].remove(todel)
                    if len(yL[yD[ny]]) == 0:
                        del yD[ny]
                    xL[xD[todel]].remove(ny)
                    if len(xL[xD[todel]]) == 0:
                        del xD[todel]

        nx -= c

print(nx, ny, ans)
    
