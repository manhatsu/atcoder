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
# from icecream import # ic

N = int(input())
if N < 2*(3**3):
    print(0)
    exit()
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# 素数列挙 O(NloglogN) つまり、素数の個数はloglogN個
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

L = getprimes(int(pow(N, 1/3)+1))

ans = 0

for q in L:
    max_p = N // (q**3)
    max_p = min(max_p, q-1)
    ans += bisect_right(L, max_p)

print(ans)