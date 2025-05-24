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

# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

F = []
for i in range(8):
    S = input()
    F.append(S)
    
G = [[0]*8 for i in range(8)]

for i in range(8):
    for j in range(8):
        if F[i][j] == '.':
            continue
        for k in range(8):
            G[k][j] = 1
        for k in range(8):
            G[i][k] = 1

ans = 0
for i in range(8):
    for j in range(8):
        if G[i][j] == 0:
            ans += 1

print(ans)
