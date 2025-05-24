from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from multiprocessing.pool import MapResult
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
import heapq
import copy
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
C = list(map(int, input().split()))
K = []
D = [[0]*M for _ in range(N)]

for m in range(M):
    L = list(map(int, input().split()))
    K.append(L[0])
    B = [l-1 for l in L[1:]]
    for b in B:
        D[b][m] = 1
    
A = []
for i in range(N):
    A.append(''.join(map(str, D[i])))

 #ic(A)

dp = {'2'*M: 0}
for i in range(2*N):
    j = i % N
    new_dp = {}
    for key, val in dp.items():
        key_flag = ['0' if k == '0' else '1' for k in key]
        key_flag = ''.join(key_flag)
        if int(key_flag, 2) & int(A[j], 2) == 0:
                continue
        new_key = ''
        for k in range(M):
            if key[k] == '0':
                new_key += '0'
                continue
            if A[j][k] == '1':
                new_key += str(int(key[k]) - 1)
            else:
                new_key += key[k]
        if new_key in dp:
            temp = min(dp[new_key], val + C[j])
        else:
            temp = val + C[j]
        if new_key in new_dp:
            new_dp[new_key] = min(new_dp[new_key], temp)
        else:
            new_dp[new_key] = temp
    dp.update(new_dp)

# ic(dp)
print(dp['0'*M])
    

