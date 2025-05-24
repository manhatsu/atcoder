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

ans = 0
tomove = 0

total_1s = 0
for i in range(len(S)):
    if S[i] == '1':
        total_1s += 1

Q1 = []
for i in range(len(S)):
    if S[i] == '1':
        if len(Q1) == 0:
            Q1.append((i, 1, 0)) # idx, kosuu, sousa
        else:
            lasti, lastk, lasts = Q1[-1]
            nexk = lastk + 1
            nexs = (i - 1 - lasti)*lastk + lasts
            Q1.append((i, nexk, nexs))

Q2 = []
for i in reversed(range(len(S))):
    if S[i] == '1':
        if len(Q2) == 0:
            Q2.append((i, 1, 0)) # idx, kosuu, sousa
        else:
            lasti, lastk, lasts = Q2[-1]
            nexk = lastk + 1
            nexs = (lasti - 1 - i)*lastk + lasts
            Q2.append((i, nexk, nexs))

Q1 = deque(Q1)
Q2 = deque(Q2)
A1 = [(0, 0)]*len(S)
A2 = [(0, 0)]*len(S)

while Q1:
    idx, k, s = Q1.popleft()
    A1[idx] = (k, s)
    while True:
        idx += 1
        s += k
        if not Q1 or idx >= Q1[0][0]:
            break
        A1[idx] = (k, s)
    
while Q2:
    idx, k, s = Q2.popleft()
    A2[idx] = (k, s)
    while True:
        idx -= 1
        s += k
        if not Q2 or idx <= Q2[0][0]:
            break
        A2[idx] = (k, s)

ans = INF
for i in range(len(S)-1):
    k1, s1 = A1[i]
    k2, s2 = A2[i+1]
    if k1 + k2 == total_1s:
        ans = min(ans, s1 + s2)

if A2[0][0] == total_1s:
    ans = min(ans, A2[0][1])
if A1[-1][0] == total_1s:
    ans = min(ans, A1[-1][1])

print(ans)  

