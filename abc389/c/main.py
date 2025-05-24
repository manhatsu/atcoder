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

Q = int(input())
# N, K = map(int, input().split())

L = SortedList()

toadd = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if len(L) == 0:
            L.add((toadd, query[1]))
        else:
            last_atama, last_length = L[-1]
            L.add((last_atama+last_length, query[1]))
    elif query[0] == 2:
        idx, length = L.pop(0)
        toadd += length
    else:
        k = query[1]-1
        print(L[k][0]-toadd)
    # print(L)


        



