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
A = list(map(int, input().split()))

K = []
org_K = []
for i in range(Q):
    k = int(input())
    org_K.append(k)
    K.append((k, i))

toadd_list = [0]*Q

K = sorted(K)
K = deque(K)

i = 0
toadd = 0
flag = False
while K:
    k, org_idx = K.popleft()
    k += toadd
    while i < N and A[i] <= k:
        toadd += 1
        i += 1
        k += 1
        if i >= N:
            break
    if i >= N:
        K.appendleft((k, org_idx))
        flag = True
        break
    toadd_list[org_idx] = toadd

if flag:
    while K:
        _, org_idx = K.popleft()
        toadd_list[org_idx] = toadd

# print(toadd_list)
for i in range(Q):
    print(toadd_list[i] + org_K[i])




