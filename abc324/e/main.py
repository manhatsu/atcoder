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

N, T = input().split()
N = int(N)
S = []
for i in range(N):
    S.append(input())

A = []
B = []

for i in range(N):
    j = 0
    for s in S[i]:
        if j >= len(T):
            break
        if s == T[j]:
            j += 1
    A.append(j)

    j = 0
    for s in S[i][::-1]:
        if j >= len(T):
            break
        if s == T[len(T)-1-j]:
            j += 1
    B.append(j)

B = sorted(B)

# print(A)
# print(B)

ans = 0
for a in A:
    lim = len(T)-a
    l = bisect_right(B, lim-1)
    ans += (N-l)

print(ans)



        
    

    



