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
A = list(map(int, input().split()))

S = []
count = 0
for i, a in enumerate(A):
    if len(S) == 0 or a != S[-1][0]:
        S.append((a, 1))
        count += 1
        print(count)
        continue
    c = S.pop()[1]
    count -= c
    c += 1
    if c == a:
        print(count)
        continue
    S.append((a, c))
    count += c
    print(count)




    
