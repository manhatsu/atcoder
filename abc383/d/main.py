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

N = int(input())

M = int(math.sqrt(N))

L = int(math.pow(N, 1/8))

# print('M', M)
# print('L', L)

def getprimes(n):
    if n == 0:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

P = getprimes(M)
Q = getprimes(L)

ans = 0
for i, p in enumerate(P):
    ans += max(0, bisect_right(P, M / p)-1-i)
ans += len(Q)
print(ans)