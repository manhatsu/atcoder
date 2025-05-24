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

N = int(input())
D = []
for i in range(N):
    x, l = map(int, input().split())
    D.append((x-l, x+l))

D = sorted(D, key= lambda x:x[1]) 
# print(D)

ans = 0
last_l = MINF
for i in range(len(D)):
    if D[i][0] >= last_l:
        last_l = D[i][1]
        ans += 1

print(ans)

