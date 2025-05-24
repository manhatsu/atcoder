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

N, M = map(int, input().split())
X = list(map(int, input().split()))
X = [x-1 for x in X]

A = [0]*N

ans = 0
for i in range(M-1):
    a = X[i]
    b = X[i+1]
    
    J = (b-a)%N
    G = (a-b)%N

    if J <= G:
        ans += J
        if b > a:
            A[a] += G-J
            A[b] -= G-J
        else:
            A[a] += G-J
            if b > 0:
                A[0] += G-J
                A[b] -= G-J
    else:
        ans += G
        if a > b:
            A[b] += J-G
            A[a] -= J-G
        else:
            A[b] += J-G
            if a > 0:
                A[0] += J-G
                A[a] -= J-G

S = []
temp = 0
for a in A:
    temp += a
    S.append(temp)

print(ans+min(S))