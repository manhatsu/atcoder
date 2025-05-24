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

N, M, Q = map(int, input().split())
# A = list(map(int, input().split()))

each_page = [set() for _ in range(M+1)]
all_page = set()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        each_page[query[2]].add(query[1])
    elif query[0] == 2:
        all_page.add(query[1])
    else:
        if query[1] in all_page:
            print("Yes")
            continue
        print('Yes' if query[1] in each_page[query[2]] else 'No')