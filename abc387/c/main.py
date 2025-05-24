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

L, R = map(int, input().split())

def get(M):
    ans = 0
    M = str(M)
    # i) Rが蛇数か
    ret0  = True
    for m in M[1:]:
        if int(m) >= int(M[0]):
            ret0 = False
            break
    if ret0:
        ans += 1
    
    # ii) n桁かつRとk桁目まで同じ
    for i in range(len(M)-1):
        if i == 0:
            ans += min(int(M[0]), int(M[i+1]))*(int(M[0])**(len(M)-i-2))
            continue
        if int(M[i]) >= int(M[0]):
            break
        ans += min(int(M[0]), int(M[i+1]))*(int(M[0])**(len(M)-i-2))
    
    # iii) n桁かつ0桁目から異なる
    for i in range(1, int(M[0])):
        ans += i ** (len(M)-1)

    # iv) n-1桁以下
    for i in range(len(M)-1):
        for j in range(1, 10):
            ans += j ** i

    return ans
  
# print(get(R))
# print(get(L-1))

print(get(R)-get(L-1))
        