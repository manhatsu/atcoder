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

N, W = map(int, input().split())

P = [[] for i in range(W)]
for i in range(N):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    P[x].append((y, i))

# print(*P)

R = []
Q = int(input())
for i in range(Q):
    t, b = map(int, input().split())
    b -= 1
    R.append((t, b, i))

R = sorted(R)
QT = [r[0] for r in R]
QB = [r[1] for r in R]
QI = [r[2] for r in R]

ANS = []


P = [sorted(p)[::-1] for p in P]
S = set([i for i in range(N)])

lastDeterminedIdx = 0
flag = True
sorouTime = 0
while lastDeterminedIdx < Q:
    toDiscard = set()
    for i in range(W):
        if len(P[i]) == 0:
            flag = False
            break
        time, block = P[i].pop()
        toDiscard.add(block)
        sorouTime = max(sorouTime, time)
    if not flag:
        for i in range(lastDeterminedIdx, Q):
            ANS.append(QB[i] in S)
        break
    idx = bisect_right(QT, sorouTime)
    if idx == lastDeterminedIdx:
        S -= toDiscard
        continue
    for i in range(lastDeterminedIdx, idx):
        ANS.append(QB[i] in S)
    lastDeterminedIdx = idx
    S -= toDiscard

RET = ['']*Q
for i in range(Q):
    RET[QI[i]] = "Yes" if ANS[i] else "No"

print(*RET, sep="\n")
        