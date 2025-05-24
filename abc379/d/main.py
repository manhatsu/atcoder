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

Q = int(input())
# N, K = map(int, input().split())

T = deque([])
S = deque([]) # nobiru
sum_nob = 0

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        T.append(i)
    elif q[0] == 2:
        S.append((i, q[1]))
        sum_nob += q[1]
    else:
        tocut = 0
        while T:
            t = T.popleft()
            # print('check tree', t)
            while S and t > S[0][0]:
                _, nob = S.popleft()
                sum_nob -= nob
            # print('height', sum_nob)
            if sum_nob >= q[1]:
                tocut += 1
                continue
            else:
                T.appendleft(t)
                break
        print(tocut)
