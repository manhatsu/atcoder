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
A = list(map(int, input().split()))

toadd = [[0]*31 for j in range(N)]

sum = 0
for i in range(31):
    for j in range(1, N):
        if (A[j]>>i) & 1:
            toadd[j][i] = j-1-toadd[j-1][i] + (((A[j-1]>>i) & 1) ^ 1) # かっこでくくらないと違う値になる
        else:
            toadd[j][i] = toadd[j-1][i] + (((A[j-1]>>i) & 1) ^ 0)
        # print('toadd at j={}: {}'.format(j, toadd[j][i]))
        sum += toadd[j][i]*(2**i)
    # print('til digit {}: sum={}'.format(i, sum))

print(sum)
