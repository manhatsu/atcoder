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

N, L = map(int, input().split())
A = list(map(int, input().split()))

S = [0]*(N+1)
for i in range(N):
    S[i+1] = S[i]+A[i]

def is_ok(X):
    C = [0]*(N+1)
    D = [0]*(N+1)
    l, r = 0, 1
    C[0] = 1
    D[0] = 1
    D[1] = -1
    
    for i in range(N):
        if i > 0:
            C[i] = C[i-1] + D[i]
        if C[i] == 0:
            continue

        while l < N+1 and S[l]-S[i] < X:
            l += 1
        
        if l > N:
            continue

        while r < N+1 and S[r]-S[i] <= L:
            r += 1

        D[l] += 1
        if r < N+1:
            D[r] -= 1

    C[N] = C[N-1]+D[N]
    return C[N] > 0

def bs(ok, ng): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = bs(0, L+1)
print(ans)



