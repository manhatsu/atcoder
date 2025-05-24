from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
import copy
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
S = input()
Q = int(input())
# N, K = map(int, input().split())

S = list(S)
last_update = [-1]*N
last_case = None
last_all_update = -1

for i in range(Q):
    t, x, c = input().split()
    t = int(t)
    x = int(x) - 1
    if t == 1:
        S[x] = c
        last_update[x] = i
    elif t == 2:
        last_case = 'L'
        last_all_update = i
    else:
        last_case = 'U'
        last_all_update = i

S = ''.join(S)
if last_all_update != -1:
    if last_case == 'L':
        T = S.lower()
    else:
        T = S.upper()
    
    T = list(T)
    for i, l in enumerate(last_update):
        if l > last_all_update:
            T[i] = S[i]
    T = ''.join(T)

else:
    T = S

print(T)