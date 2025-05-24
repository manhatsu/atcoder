from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
# MOD = 998244353
MOD = 10**9+7
INF = float("inf")
MINF = -float("inf")

N, K = map(int, input().split())
# A = list(map(int, input().split()))

if K == 1:
    print(1)
elif N == K:
    print(1)
    for i in range(K-1):
        print(0)

else:
    def NCM(n, m):
        return math.factorial(n) // math.factorial(n-m) // math.factorial(m)

    for i in range(1, K+1):
        ans = NCM(K-1, i-1)%MOD
        if N-K+1 >= i:
            ans *= NCM(N-K+1, i)%MOD
            print(ans%MOD)
        else:
            print(0)