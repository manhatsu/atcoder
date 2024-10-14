# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, Q = map(int, input().split())
S = input()
T = list(S)

ans = 0
flag = 0
for s in S:
    if s == 'A':
        flag = 1
    elif s == 'B' and flag == 1:
        flag = 2
    elif s == 'C' and flag == 2:
        ans += 1
        flag = 0
    else:
        flag = 0

for i in range(Q):
    x, c = input().split()
    x = int(x)-1
    if T[x] == 'A':
        if x < len(T)-2:
            if T[x+1] == 'B' and T[x+2] == 'C':
                ans -= 1
    elif T[x] == 'B':
        if x > 0 and x < len(T)-1:
            if T[x-1] == 'A' and T[x+1] == 'C':
                ans -= 1
    elif T[x] == 'C':
        if x > 1:
            if T[x-2] == 'A' and T[x-1] == 'B':
                ans -= 1
    T[x] = c
    if c == 'A':
        if x < len(T)-2:
            if T[x+1] == 'B' and T[x+2] == 'C':
                ans += 1
    elif c == 'B':
        if x > 0 and x < len(T)-1:
            if T[x-1] == 'A' and T[x+1] == 'C':
                ans += 1
    elif c == 'C':
        if x > 1:
            if T[x-2] == 'A' and T[x-1] == 'B':
                ans += 1
    print(ans)