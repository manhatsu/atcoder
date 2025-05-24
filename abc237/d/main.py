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
S = input()
# A = list(map(int, input().split()))

LE = [-1]*(N+1)
RI = [-1]*(N+1)

for i in range(1, N+1):
    if S[i-1] == 'L':
        j = LE[i-1]
        LE[i] = j
        RI[i] = i-1
        LE[i-1] = i
        if j != -1:
            RI[j] = i
    else:
        j = RI[i-1]
        RI[i] = j
        LE[i] = i-1
        RI[i-1] = i
        if j != -1:
            LE[j] = i

ans = []

for i in range(N+1):
    if LE[i] == -1:
        ans.append(i)
while True:
    if RI[ans[-1]] == -1:
        break
    ans.append(RI[ans[-1]])

print(*ans)