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
L = []
for _ in range(N):
    a, b = map(int, input().split())
    L.append((a, b))

L = sorted(L, key=lambda x: x[1])

t = 0
for a, b in L:
    if t+a > b:
        print("No")
        exit()
    t += a

print("Yes")