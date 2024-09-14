# from collections import defaultdict, deque
from itertools import combinations, permutations
# import math
# import sys
# sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
# from bisect import bisect, bisect_left, bisect_right
# from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
S = list(input())
S = sorted(S)[::-1]
# print(S)

sq_num_set = [i**2 for i in range(0, 10**7+1)]
ans = 0
for sq in sq_num_set:
    T = sorted(list(str(sq)))[::-1]

    if len(S) < len(T):
        continue
    isSame = True
    for i in range(len(T)):
        if T[i] != S[i]:
            isSame = False
            break
    if len(T) < len(S):
        if any([s != '0' for s in S[len(T):]]):
            isSame = False
    if isSame:
        ans += 1
            
print(ans)