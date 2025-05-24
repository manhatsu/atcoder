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

N, S, T= map(int, input().split())

P = [(0, 0)]*(2*N)
for i in range(0, 2*N, 2):
    a, b, c, d = map(int, input().split())
    P[i] =  (a, b)
    P[i+1] = (c, d)

dist = [[0.0]*(2*N) for i in range(2*N)]
for i in range(2*N):
    for j in range(2*N):
        if i == j:
            continue
        dist[i][j] = math.sqrt((P[i][1]-P[j][1])**2 + (P[i][0]-P[j][0])**2)

dp = [[INF]*(2*N) for i in range(2**(2*N))]

# (0, 0)スタート
for i in range(2*N):
    time0 = math.sqrt(P[i][1]**2 + P[i][0]**2) / S
    if i % 2 == 0:
        time1 = dist[i][i+1] / T
        dp[(1 << i) | (1 << (i+1))][i+1] = time0 + time1
    else:
        time1 = dist[i][i-1] / T
        dp[(1 << i) | (1 << (i-1))][i-1] = time0 + time1

for i in range(2**(2*N)):
    for j in range(2*N):
        for k in range(2*N):
            if i >> k & 1:
                continue
            time0 = dist[j][k] / S
            if k % 2 == 0:
                if i >> (k+1) & 1:
                    continue
                time1 = dist[k][k+1] / T
                dp[(i | (1 << k) | (1 << (k+1)))][k+1] = \
                    min(dp[(i | (1 << k) | (1 << (k+1)))][k+1], \
                        dp[i][j] + time0 + time1)
            else:
                if i >> (k-1) & 1:
                    continue
                time1 = dist[k][k-1] / T
                dp[(i | (1 << k) | (1 << (k-1)))][k-1] = \
                    min(dp[(i | 1 << k | 1 << (k-1))][k-1], \
                        dp[i][j] + time0 + time1)

ans = INF            
for i in range(2*N):
    if dp[2**(2*N)-1][i] < ans:
        ans = dp[2**(2*N)-1][i]

print(ans)
    
        
            

 

