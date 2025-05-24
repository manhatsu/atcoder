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

# 約数列挙 O(√N)
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

D = dict()

for a in A:
    if not a in D:
        D[a] = 1
    else:
        D[a] += 1

ans = 0
for k, v in D.items():
    L = make_divisors(k)
    for l in L:
        if l in D and k // l in D:
            ans += v * D[l] * D[k//l]

print(ans)