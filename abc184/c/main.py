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

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
# A = list(map(int, input().split()))

R = abs(r2-r1)
C = abs(c2-c1)

if R == 0 and C == 0:
    ans = 0
elif R+C <= 3 or R == C:
    ans = 1
else:
    rem = R-C
    if abs(R-C) <= 3 or (R-C)%2 == 0:
        ans = 2
    else:
        ans = 3

print(ans)