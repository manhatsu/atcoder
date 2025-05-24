from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from operator import is_
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

A, B = map(int, input().split())

f = lambda x: B*x + A / math.sqrt(x+1)

ans = INF
for x in range(max(0, math.floor(pow(2*B/A, -2/3))-1-5), math.ceil(pow(2*B/A, -2/3))-1+5):
    ans = min(ans, f(x))

print('{:.10f}'.format(ans))