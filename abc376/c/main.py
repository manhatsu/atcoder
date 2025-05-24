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
B = list(map(int, input().split()))

A = sorted(A)[::-1]
B = sorted(B)[::-1]

flag = 0
x = -1
ret = True
for i in range(N):
    if i == N-1 and flag == 0:
        x = A[N-1]
        break
    j = i+flag
    if A[i] <= B[j]:
        continue
    if flag == 0:
        x = A[i]
        flag = -1
        continue
    if flag < 0:
        ret = False
        break

print(x if ret else -1)




