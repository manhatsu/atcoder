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

evens = 0
odds = 0
for i in range(N):
    s = input()
    s = int(s, 2)
    if s.bit_count() % 2 == 0:
        evens += 1
    else:
        odds += 1

print(evens * odds)

        
