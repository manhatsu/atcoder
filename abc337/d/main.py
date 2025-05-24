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

H, W, K = map(int, input().split())
F = []
for i in range(H):
    F.append(input())

def getNChange(L):
    num_o_dot = 0
    num_dot = 0
    cur = 0
    ans = INF
    while cur < len(L):
        if L[cur] == 'o':
            cur += 1
            num_o_dot += 1
        elif L[cur] == '.':
            cur += 1
            num_dot += 1
            num_o_dot += 1
        else:
            cur += 1
            num_dot = 0
            num_o_dot = 0
        if num_o_dot == K:
            ans = min(ans, num_dot)
            num_o_dot -= 1
            if L[cur-K] == '.':
                num_dot -= 1
    return ans
            

ans = INF
for i in range(H):
    L = F[i]
    ans = min(ans, getNChange(L))

for j in range(W):
    L = []
    for i in range(H):
        L.append(F[i][j])
    ans = min(ans, getNChange(L))

print(ans if ans != INF else -1)