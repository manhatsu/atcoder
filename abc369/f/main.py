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

H, W, N = map(int, input().split())
coin_pos = []
for i in range(N):
    r, c = map(int, input().split())
    coin_pos.append([r, c])

sorted_coin_pos_0 = sorted(coin_pos)
temp = [[l[1], l[0]] for l in coin_pos]
s_temp = sorted(temp)
sorted_coin_pos_1 = [[l[1], l[0]] for l in s_temp]
# sorted_coin_pos_1 = sorted(coin_pos, key=lambda x: x[1])
# print(sorted_coin_pos_1)

ans_0 = ''
ncoins_0 = 0
prev_r = 1
prev_c = 1
for l in sorted_coin_pos_0:
    r, c = l[0], l[1]
    if c < prev_c:
        continue
    ncoins_0 += 1
    ans_0 += 'D'*(r-prev_r)
    ans_0 += 'R'*(c-prev_c)
    prev_r = r
    prev_c = c

ans_0 += 'D'*(H-prev_r)
ans_0 += 'R'*(W-prev_c)

ans_1 = ''
ncoins_1 = 0
prev_r = 1
prev_c = 1
for l in sorted_coin_pos_1:
    r, c = l[0], l[1]
    if r < prev_r:
        continue
    ncoins_1 += 1
    ans_1 += 'D'*(r-prev_r)
    ans_1 += 'R'*(c-prev_c)
    prev_r = r
    prev_c = c

ans_1 += 'D'*(H-prev_r)
ans_1 += 'R'*(W-prev_c)

if ncoins_0 > ncoins_1:
    # print('print0')
    print(ncoins_0)
    print(ans_0)
else:
    print(ncoins_1)
    print(ans_1)  

