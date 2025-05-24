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
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = [(b, i) for i, b in enumerate(B)]

taberuhito = [-1]*M

S = sorted(S)
T = [s[0] for s in S]

eaten = M
for i in range(N):
    ok = bisect_left(T, A[i])
    if ok < eaten:
        for j in range(ok, eaten):
            taberuhito[j] = i
        eaten = ok

# print(taberuhito)
T = [(s[1], t) for t, s in zip(taberuhito, S)]
T = sorted(T)
# print(T)

for i in range(M):
    print(-1 if T[i][1] == -1 else T[i][1]+1)