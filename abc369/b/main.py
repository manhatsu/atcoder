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

N = int(input())

fatigue_l = -1
nowl = -1
fatigue_r = -1
nowr = -1

for i in range(N):
    L = list(input().split())
    a = int(L[0])
    s = L[1]
    if s == 'L':
        if fatigue_l == -1:
            fatigue_l = 0
            nowl = a
        else:
            fatigue_l += abs(a-nowl)
            nowl = a
    else:
        if fatigue_r == -1:
            fatigue_r = 0
            nowr = a
        else:
            fatigue_r += abs(a-nowr)
            nowr = a

if fatigue_l == -1:
    fatigue_l = 0
if fatigue_r == -1:
    fatigue_r = 0
print(fatigue_l + fatigue_r)