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

N, D = map(int, input().split())
S = input()

C = []
for i, s in enumerate(S):
    if s == '@':
        C.append(i)
    
for _ in range(D):
    C.pop()

C = set(C)

ans = ''
for i in range(len(S)):
    if i in C:
        ans += '@'
    else:
        ans += '.'

print(ans)

