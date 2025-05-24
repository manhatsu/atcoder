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
B = [[-1, A[i]] for i in range(N)]

last_all_updated = -1
offset = 0
Q = int(input())
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        last_all_updated = i
        offset = q[1]
    elif q[0] == 2:
        idx = q[1]-1
        if B[idx][0] < last_all_updated:
            B[idx][0] = i
            B[idx][1] = q[2]
        else:
            B[idx][1] += q[2]
    else:
        idx = q[1]-1
        if B[idx][0] < last_all_updated:
            B[idx][0] = i
            B[idx][1] = 0
        print(offset+B[idx][1])
