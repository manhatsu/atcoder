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

# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

def getprimes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

primes = getprimes(10**6)

S = [0]*(10**6+1)

for p in primes:
    for bp in range(p, 10**6+1, p):
        S[bp] += 1

N20 = [s for s in range(10**6+1) if S[s] == 2]
N400 = [s**2 for s in N20]


Q = int(input())
for _ in range(Q):
    A = int(input())
    idx = bisect_right(N400, A)
    print(N400[idx-1])