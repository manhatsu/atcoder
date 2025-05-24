from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from ssl import VerifyFlags
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, R, C = map(int, input().split())
# A = list(map(int, input().split()))
S = input()

dx = {'N':0, 'S':0, 'W':-1, 'E':1}
dy = {'N':-1, 'S':1, 'W':0, 'E':0}

Ax = [0]*(N+1)
Ay = [0]*(N+1)

for i in range(N):
    Ax[i+1] = Ax[i] + dx[S[i]]
    Ay[i+1] = Ay[i] + dy[S[i]]

seen = defaultdict(list)
seen[(0, 0)].append(0)


ret = set()

for i in range(1, N+1):
    target = (Ay[i]-R, Ax[i]-C)

    if target in seen:
        ret.add(i)
    
    seen[(Ay[i], Ax[i])].append(i)

ans = ''
for i in range(1, N+1):
    if i in ret:
        ans += '1'
    else:
        ans += '0'

print(ans)




