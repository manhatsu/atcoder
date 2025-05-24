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

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
temp = 0
for a in A:
    temp += a
    S.append(temp)

N += 1
ret = False
for i in range(N-3):
    O = S[i]
    j = bisect_left(S, O+P)
    if j >= N-2:
        continue
    if S[j] != O+P:
        continue
    k = bisect_left(S, S[j]+Q)
    if k >= N-1:
        continue
    if S[k] != O+P+Q:
        continue
    l = bisect_left(S, S[k]+R)
    if l >= N:
        continue
    if S[l] != O+P+Q+R:
        continue
    ret = True
    break

print('Yes' if ret else 'No')