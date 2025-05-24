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
P = list(map(int, input().split()))
P = [p-1 for p in P]

ans = []
for i in range(N):
    for j in range(N-2):
        if P[j+2] %2 != (j+2) % 2 and P[j] %2 == j % 2:
            P[j], P[j+2] = P[j+2], P[j]
            ans.append(('B', j))

for i in range(0, N, 2):
    if P[i] % 2 != i % 2:
        P[i], P[i+1] = P[i+1], P[i]
        ans.append(('A', i))

for i in range(N):
    for j in range(N-2):
        if P[j] > P[j+2]:
            P[j], P[j+2] = P[j+2], P[j]
            ans.append(('B', j))

ans = [(s, i+1) for s, i in ans]

print(len(ans))
for a in ans:
    print(*a)