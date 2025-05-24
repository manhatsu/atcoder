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
# N, K = map(int, input().split())
T = list(map(int, input().split()))

now = 0

for t in T:
    u = now // (2 ** t)
    if u % 2 == 0:
        v = u+1
    else:
        v = u+2
    now = 2 ** t * v

print(now)