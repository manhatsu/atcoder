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
# A = list(map(int, input().split()))
S = input()

D = defaultdict(int)

D[int(S[0])] += 1
ans = D[1]

if N > 1:
    for s in S[1:]:
        s = int(s)
        if s:
            D[0], D[1] = D[1], D[0]
            D[1] += 1
        else:
            D[1] += D[0]
            D[0] = 1
        ans += D[1]

print(ans)
