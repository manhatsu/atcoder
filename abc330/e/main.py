# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
from sortedcontainers import SortedList, SortedDict, SortedSet
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, Q = map(int, input().split())
A = list(map(int, input().split()))

D = defaultdict(int)

for a in A:
    D[a] += 1

M = set([i for i in range(N+1)]) - set(A)
M = SortedList(M)

for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1

    temp = A[i]
    A[i] = x

    if D[temp] > 0:
        D[temp] -= 1
        if D[temp] == 0:
            M.add(temp)
    D[x] += 1
    if D[x] == 1:
        M.discard(x)

    print(M[0])

    


