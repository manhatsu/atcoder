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

# ダブリングではうまくいかない

N, K = map(int, input().split())
P = list(map(int, input().split()))

if K == 0:
    print(*P)

else:
    for i in range(min(K+1, 2*10**5+1)):
        