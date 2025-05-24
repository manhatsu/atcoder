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

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

total_length = sum(A)

X = [0]
Y = [0]

S = [0]
T = [0]

x = 0
y = 0
s = 0
t = 0
for i in range(N):
    x += A[i]
    y += A[N-1-i]
    s += A[i]/B[i]
    t += A[N-1-i]/B[N-1-i]
    X.append(x)
    Y.append(y)
    S.append(s)
    T.append(t)

i = 0
j = 0
while X[i] + Y[j] < total_length:
    if S[i] <= T[j]:
        i += 1
    else:
        j += 1

# print(i, j)

if S[i] <= T[j]:
    rem = A[N-j] - (S[i]-T[j-1]) * B[N-j]
    # print((X[i], rem))
    ans = X[i]+rem/2
else:
    rem = A[i-1] - (T[j]-S[i-1]) * B[i-1]
    # print((X[i], rem))
    ans = X[i-1] + rem/2 + (T[j]-S[i-1]) * B[i-1]

print(ans)
    
    


