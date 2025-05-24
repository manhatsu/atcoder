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

temp_minus_val = 0
Q = SortedList([])
res = []

for i in range(N):
    while len(Q) >0:
        if  Q[0] == i:
            Q.pop(0)
            temp_minus_val += 1
        else:
            break
    toadd = i - temp_minus_val
    tosubtract = len(A)-i-1

    new_val = A[i] + toadd - tosubtract
    if new_val < 0:
        Q.add(len(A)+new_val)
        res.append(0)
    else:
        res.append(new_val)

print(*res)