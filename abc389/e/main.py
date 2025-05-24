from collections import defaultdict, deque
import glob
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

N, M = map(int, input().split())
P = list(map(int, input().split()))

K = 0

def isOK(x):
    global K
    k = 0
    m = 0
    temp_xplus1 = 0
    for p in P:
        j = (x+p) // (2*p)
        k += j
        m += j**2*p
        if (2*(j+1)-1)*p == x+1:
            temp_xplus1 += 1
        if m > M: # 途中で打ち切らないとオーバーフローする
            break
    if m > M:
        return False
    else:
        k += min((M-m)//(x+1), temp_xplus1)
        K = max(K, k)
        return True
    
def bs(ok, ng):
    global K
    if abs(ok - ng) <= 1:
        return ok
    mid = (ok + ng) // 2
    if isOK(mid):
        return bs(mid, ng)
    else:
        return bs(ok, mid)
    
bs(0, M+1)
print(K)