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
# A = list(map(int, input().split()))

K = []
connect = []
for i in range(M):
    L = list(map(int, input().split()))
    K.append(L[0])
    L = [x-1 for x in L[1:]]
    c = 0
    for l in L:
        c += 1 << l
    connect.append(c)

P = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    ret = True
    for j in range(M):
        if int.bit_count(i & connect[j]) % 2 != P[j]:
            ret = False
            break
    if ret:
        ans += 1

print(ans)
