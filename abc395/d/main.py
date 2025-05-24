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

N, Q = map(int, input().split())

D = dict()
su_taiou = [i for i in range(N)]
E = [i for i in range(N)] # su_taiouの逆

for i in range(N):
    D[i] = i

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1]-1, query[2]-1
        D[a] = su_taiou[b]
    
    elif query[0] == 2:
        a, b = query[1]-1, query[2]-1
        su_taiou[a], su_taiou[b] = su_taiou[b], su_taiou[a]
        E[su_taiou[a]], E[su_taiou[b]] = a, b
    
    else:
        a = query[1]-1
        print(E[D[a]]+1)