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

N, Q = map(int, input().split())

C = [1]*N
D = dict()
S = SortedSet([i for i in range(N)])
for i in range(N):
    D[i] = i

for i in range(Q):
    # print('phase', i)
    q = list(map(int, input().split()))
    if q[0] == 2:
        c = q[1]-1
        print(C[c])
    else:
        x = q[1]-1
        c = q[2]-1
        # print('query 1: x={}, c={}'.format(x, c))
    
        lidx = S.bisect_right(x)-1
        L = S[lidx]
        R = N
        if lidx < len(S)-1:
            R = S[lidx+1]
        # print('L:', L, 'R:', R)
        C[D[L]] -= R-L
        D[L] = c
        C[D[L]] += R-L
        # print('number of blocks with each color')
        # print(*C)

        if lidx < len(S)-1:
            if D[L] == D[R]:
                S.discard(R)
        if lidx > 0:
            if D[L] == D[S[lidx-1]]:
                S.discard(L)

        




