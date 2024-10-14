from collections import defaultdict, deque, Counter
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

K = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

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

A = prime_factorization(K)
# print(A)
ans = 2

for (d, j) in A:
    for i in range(d, d*50, d):
        h = i
        while h % d == 0:
            h //= d
            j -= 1
        if j <= 0:
            break
    if i > ans:
        ans = i

print(ans)
