from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
from atcoder.fenwicktree import FenwickTree
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

order = 'atcoder'

D = {c:i for i, c in enumerate(order)}

F = FenwickTree(len(S))

ans = 0
for s in S:
    F.add(D[s], 1)
    ans += F.sum(D[s]+1, len(order))

print(ans)



