# from collections import defaultdict, deque
from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
d = [[INF]*N for i in range(N)] # 距離
for i in range(N):
    d[i][i] = 0

A = []

for i in range(M):
    u, v, c = map(int, input().split())
    u, v = u-1, v-1
    A.append((u, v, c))
    d[u][v] = min(d[u][v], c)
    d[v][u] = min(d[v][u], c)

# 最短距離更新
for k in range(N): # 経由する点
    for i in range(N): # 始点
        for j in range(N): # 終点
            d[i][j] = min(d[i][k]+d[k][j], d[i][j])

def getMinDist(d, A, K, B): # K: 指定した橋の数、B: 指定した橋番号
    ans = INF
    b_orders = list(permutations(B))
    for b_order in b_orders: # 順番 K!通り
        for i in range(2**K): # 向き 2**K通り
            temp_ans = 0
            prev_v = 0
            for j in range(K):
                u, v, c = A[b_order[j]]
                if (i >> j) & 1: # 1が立ってたら逆向きにする(v -> u)
                    if prev_v != v:
                        temp_ans += d[prev_v][v]
                    temp_ans += c
                    prev_v = u
                else:
                    if prev_v != u:
                        temp_ans += d[prev_v][u]
                    temp_ans += c
                    prev_v = v
            # 最後にノードN-1までの距離を足す
            if prev_v != N-1:
                temp_ans += d[prev_v][N-1]
            # 最小の場合更新
            if temp_ans < ans:
                ans = temp_ans

    return ans
   
Q = int(input())
# print('num of query:', Q)
for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    B = [b-1 for b in B]
    # print(K, B)
    out = getMinDist(d, A, K, B)
    print(out)



