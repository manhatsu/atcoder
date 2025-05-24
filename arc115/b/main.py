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

C = []
for _ in range(N):
    C.append(list(map(int, input().split())))

B = C[0]
A = [C[i][0] - B[0] for i in range(N)]

ret = True
if min(A) < 0:
    if min(B) < -min(A):
        ret = False
    else:
        ret = True
        offsetA = min(A)
        A = [a - offsetA for a in A]
        B = [b + offsetA for b in B]

if ret:
    for i in range(N):
        for j in range(N):
            if C[i][j] != A[i] + B[j]:
                ret = False
                break
        if not ret:
            break

if ret:
    print('Yes')
    print(*A)
    print(*B)
else:
    print('No')
