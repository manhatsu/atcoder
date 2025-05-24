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
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

L = make_divisors(8*N)

ans = 0
found_n2_set = set()
for l in L[:len(L)//2]:
    if l % 2 != 0:
        continue
    r = 8*N//l
    if r % 2 != 0:
        continue
    c2 = (l + r)
    if c2 % 2 != 0:
        continue
    c = c2 // 2
    if c % 2 == 0 or c < 0:
        continue
    b = l - c

    n2 = -b + c
    if n2 <= 0 or n2 % 2 != 0:
        continue
    if n2 in found_n2_set:
        continue
    found_n2_set.add(n2)
    ans += 1

    if b != 0:
        n2 = b + c
        if n2 <= 0 or n2 % 2 != 0:
            continue
        if n2 in found_n2_set:
            continue    
        found_n2_set.add(n2)
        ans += 1        

print(ans)