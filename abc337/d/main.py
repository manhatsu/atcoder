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

def getMinNChanges(S):
    i, j = 0, 0
    num_o, num_p = 0, 0
    min_nchanges = K+1

    while(i<=len(S)-K):
        reset_flag = False
        end_flag = False
        while(num_o+num_p < K):
            if j >= len(S):
                end_flag = True
                break
            if S[j] == 'x':
                num_o = 0
                num_p = 0
                reset_flag = True
                j += 1
                break
            if S[j] == 'o':
                num_o += 1
                j += 1
                continue
            if S[j] == '.':
                num_p += 1
                j += 1
                continue
        if end_flag:
            break
        if reset_flag:
            i = j
            continue
        if num_p < min_nchanges:
            min_nchanges = num_p
        if S[i] == 'o':
            num_o -= 1
        elif S[i] == '.':
            num_p -= 1
        # elif S[i] == 'x':
            # print('!!Bug found!!')
            # print('i:', i, 'j:', j)
        i += 1
    return min_nchanges

ans = K+1
# 横方向探索
for h in range(H):
    S = F[h]
    temp = getMinNChanges(S)
    if temp < ans:
        ans = temp
# 縦方向
for w in range(W):
    # print(w)
    S = [f[w] for f in F]
    # print('S:', S)
    temp = getMinNChanges(S)
    if temp < ans:
        ans = temp

print(-1 if ans == K+1 else ans)