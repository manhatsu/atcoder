from collections import defaultdict, deque
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

S = input()
T = input()

S = list(S)
T = list(T)

Q = []
R = []
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    if ord(S[i]) < ord(T[i]):
        R.append(i)
    else:
        Q.append(i)

# print(Q)
# print(R)

X = []
for q in Q:
    S[q] = T[q]
    X.append(S.copy())

for r in R[::-1]:
    S[r] = T[r]
    X.append(S.copy())

print(len(X))
for x in X:
    out = ''.join(x)
    print(out)
