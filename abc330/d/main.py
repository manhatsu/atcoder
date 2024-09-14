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

F = []

for i in range(N):
    F.append(input())

h_sum = [0]*N
w_sum = [0]*N

for i in range(N):
    for j in range(N):
        if F[i][j] == 'o':
            h_sum[i] += 1
            w_sum[j] += 1

# print(h_sum)
# print(w_sum)

ans = 0
for i in range(N):
    for j in range(N):
        # print('i, j', i, j)
        if F[i][j] == 'x':
            continue
        if h_sum[i] == 1 or w_sum[j] == 1:
            continue
        if F[i][j] == 'o':
            ans += (h_sum[i]-1)*(w_sum[j]-1)
        # print(ans)

print(ans)