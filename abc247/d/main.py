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

Q = deque()
for i in range(N):
    q = list(map(int, input().split()))
    if q[0] == 1:
        Q.append((q[1], q[2]))
    else:
        c = q[1]
        ret = 0
        while c > 0 and Q:
            a, b = Q.popleft()
            if c >= b:
                c -= b
                ret += b * a
            else:
                b -= c
                Q.appendleft((a, b))
                ret += c * a
                c = 0
        print(ret)
    # print(Q)