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

H, W = map(int, input().split())

A = []
B = []
for i in range(H):
    A.append(list(map(int, input().split())))
for i in range(H):
    B.append(list(map(int, input().split())))

Hs = [i for i in range(H)]
Ws = [i for i in range(W)]

h_orders = list(permutations(Hs))
w_orders = list(permutations(Ws))

ans = 10**6
for h_order in h_orders:
    for w_order in w_orders:
        Adash = [[0]*W for i in range(H)]
        for i, h in enumerate(h_order):
            for j, w in enumerate(w_order):
                Adash[i][j] = A[h][w]

        if Adash != B:
            continue

        # 転倒数（昇順に戻すまでに何回入れ替えが必要か）
        h_tentou, w_tentou = 0, 0
        for i, h in enumerate(h_order):
            h_tentou += sum([h > lh for lh in h_order[i+1:]])
        for j, w in enumerate(w_order):
            w_tentou += sum([w > lw for lw in w_order[j+1:]])

        if ans > h_tentou + w_tentou:
            ans = h_tentou + w_tentou

print(ans if ans != 10**6 else -1)