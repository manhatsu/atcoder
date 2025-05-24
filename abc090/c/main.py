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

N, M = map(int, input().split())

ans = 0
if N == 1 and M == 1:
    ans = 1
elif N == 1 or M == 1:
    ans = N*M-2
else:
    ans = N*M-(N-1)*2-(M-1)*2

print(ans)