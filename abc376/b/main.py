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

L = 0
R = 1
ans = 0

for i in range(Q):
    h, t = input().split()
    t = int(t)-1
    if h == 'L':
        if t == L:
            continue
        jun = (t-L)%N
        gyaku = (L-t)%N
        if jun <= gyaku: # jun
            for i in range(1, jun+1):
                if (L+i)%N == R:
                    jun = INF
                    break
        else:
            for i in range(1, gyaku+1):
                if (L-i)%N == R:
                    gyaku = INF
                    break
        if jun <= gyaku:
            ans += jun
        else:
            ans += gyaku
        L = t

    else:
        if t == R:
            continue
        jun = (t-R)%N
        gyaku = (R-t)%N

        if jun <= gyaku: # jun
            for i in range(1, jun+1):
                if (R+i)%N == L:
                    jun = INF
                    break
        else: # gyaku
            for i in range(1, gyaku+1):
                if (R-i)%N == L:
                    gyaku=INF
                    break
        if jun <= gyaku:
            ans += jun
        else:
            ans += gyaku
        R = t

print(ans)



