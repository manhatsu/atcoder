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

N = int(input())
# N, K = map(int, input().split())
B = []
for i in range(N):
    A = map(int, input().split())
    A = [a-1 for a in A]
    B.append(A)

# print(B)

now = 0
for i in range(N):
    if now >= i:
        now = B[now][i]
    else:
        now = B[i][now]

print(now+1)


    
