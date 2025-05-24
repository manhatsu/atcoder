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
A = list(map(int, input().split()))

ans = set()
S = []

def dfs(v, S):
    if v == N:
        a = S[0]
        for i in range(1, len(S)):
            a ^= S[i]
        ans.add(a)
        return
    for i in range(len(S)):
        S[i] += A[v]
        dfs(v+1, S)
        S[i] -= A[v]
    S.append(A[v])
    dfs(v+1, S)
    S.pop()

dfs(0, S)
# print(*ans)
print(len(ans))