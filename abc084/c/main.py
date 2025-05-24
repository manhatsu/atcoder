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

if N == 1:
    print(0)
else:
    E = [[0, 0, 0]]
    for i in range(N-1):
        c, s, f = map(int, input().split())
        E.append([c, s, f])

    T = [[0]*N for i in range(N)]

    for i in range(1, N):
        for j in range(i):
            if T[j][i-1] < E[i][1]:
                T[j][i] = E[i][0]+E[i][1]
            else:
                if T[j][i-1] % E[i][2] == 0:
                    T[j][i] = T[j][i-1] + E[i][0]
                else:
                    T[j][i] = T[j][i-1] + (E[i][2] - (T[j][i-1] % E[i][2])) + E[i][0]

    for i in range(N):
        # print(*T[i])
        print(T[i][N-1])
