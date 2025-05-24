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

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

S = []
stemp = 0

for i in range(N):
    stemp += L-A[i]
    S.append(stemp)

T = []
ttemp = 0
for i in reversed(range(N)):
    ttemp += R-A[i]
    T.append(ttemp)
T = T[::-1]

SS = SortedList([0])
TT = SortedList(T)
TT.add(0)

ans = TT[0]
for i in range(N):
    SS.add(S[i])
    TT.discard(T[i])
    ans = min(ans, SS[0]+TT[0])

print(sum(A) + ans)