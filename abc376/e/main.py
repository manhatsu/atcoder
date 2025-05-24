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

T = int(input())
# N, K = map(int, input().split())

def F(N, K, A, B):
    Z = zip(A, B)
    Z = sorted(Z)
    A, B = zip(*Z)

    # print(A)
    # print(B)

    if K == 1:
        return min([a*b for a, b in zip(A, B)])

    min_val = INF
    C = SortedList(B[:K-1])
    v = sum(C)
    for j in range(K-1, N):
        if j > K-1:
            if B[j-1] < C[-1]:
                v -= C[-1]
                v += B[j-1]
                C.pop()
                C.add(B[j-1])
        temp = A[j]*(B[j]+v)
        if temp < min_val:
            min_val = temp

    return min_val

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(F(N, K, A, B))



