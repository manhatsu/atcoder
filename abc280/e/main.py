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

N, P = map(int, input().split())
# A = list(map(int, input().split()))

kaijo = [1]*(N+1)
for i in range(1, N+1):
    kaijo[i] = kaijo[i-1]*i%MOD

def nCk(n, k):
    return kaijo[n]*pow(kaijo[k], -1, MOD)*pow(kaijo[n-k], -1, MOD)%MOD

two_p_ruijo = [1]*(N+1)
one_p_ruijo = [1]*(N+1)
for i in range(1, N+1):
    two_p_ruijo[i] = two_p_ruijo[i-1]*P*pow(100, -1, MOD)%MOD
    one_p_ruijo[i] = one_p_ruijo[i-1]*(1-P*pow(100, -1, MOD))%MOD

def F(n, k):
    if n-k < 0 or 2*k-n < 0:
        return 0
    return nCk(k, n-k)%MOD * two_p_ruijo[n-k]%MOD*one_p_ruijo[2*k-n]%MOD

ans = 0
for K in range(math.ceil(N/2), N+1):
    temp = F(N-1, K-1) + F(N-2, K-1)*two_p_ruijo[1]
    temp %= MOD
    ans = (ans + temp*K)%MOD

print(ans)

    
