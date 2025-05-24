from collections import defaultdict, deque
from itertools import product
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
Y = M - (10*N - 9)

A = [(str(i), i) for i in range(Y+1)]
for i in range(N-1):
    temp = A
    newA = []
    for i in range(Y+1):
        for a, s in temp:
            if i+s <= Y:
                newa = str(i)+a
                newA.append((newa, i+s))
    A = newA

print(len(A))
ans = []
for string, _ in A:
    L = list(string)
    subans = []
    toappend = 1
    for i, a in enumerate(L):
        toadd = int(a)
        toappend += toadd
        subans.append(toappend)
        toappend += 10
    ans.append(subans)

for a in ans:
    print(*a)

def distribute(y, n):
    all_distributions = []
    for T in range(y + 1):
        for distribution in product(range(T + 1), repeat=n):
            if sum(distribution) == T:
                all_distributions.append(distribution)
    return all_distributions



