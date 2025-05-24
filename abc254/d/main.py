from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
# from icecream import # ic
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

def isSquare(n):
    return n == int(n**0.5)**2

square_numbers = set()
for i in range(1, 10**5+1):
    square_numbers.add(i**2)

# 約数列挙 O(√N)
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

def f(n): # nの約数のうち最大の平方数
    divisors = make_divisors(n)[::-1]
    for d in divisors:
        if d in square_numbers:
            return d
    return 1

i_invfi = [0]*(N+1)
for i in range(1, N+1):
    i_invfi[i//f(i)] += 1

ans = 0
for i in range(1, N+1):
    ans += i_invfi[i] ** 2

print(ans)

