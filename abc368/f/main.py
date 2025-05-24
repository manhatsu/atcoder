# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

def prime_factorization(N):
    a = []
    cnt = 0
    while (N >= 2 and N % 2 == 0):
        N //= 2
        cnt += 1
    if cnt > 0:
        a.append([2, cnt])
    q = 3
    for i in range(int(q), int(N ** 0.5)+1, 2):
        cnt = 0
        while (N % i == 0):
            N //= i
            cnt += 1
        if cnt > 0:
            a.append([i, cnt])
    if N > 1:
        a.append([N, 1])
    return a

def D(N):
    A = prime_factorization(N)
    ret = 0
    for _, a in A:
        ret += a

    return ret

sumxor = 0
for a in A:
    p = D(a)
    sumxor ^= p

print('Bruno' if sumxor == 0 else 'Anna')