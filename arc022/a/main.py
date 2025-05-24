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

S = input()

tosearch = "ICT"
now = 0
for s in S:
    if s == tosearch[now] or s == tosearch[now].lower():
        now += 1
        if now == 3:
            break

print("YES" if now == 3 else "NO")