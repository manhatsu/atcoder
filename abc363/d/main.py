# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
# from bisect import bisect, bisect_left, bisect_right
# from collections import defaultdict, deque
MOD = 998244353
# INF = float("inf")
# MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

temp = 0
for d in range(10**7):
    temp1 = temp
    if d == 0:
        temp = 1
    else:
        if d%2 == 0:
            temp += 9*10**(d//2-1)
        else:
            temp += 9*10**(d//2)
    if temp >= N:
        break

# dが求める回文数の桁数、temp1番目が(d-1)桁の最大の回文数

if d == 0:
    T = '0'
elif d%2 == 0:
    S = str(N-temp1+10**(d//2-1)-1)
    T = S + S[::-1]
else:
    S = str(N-temp1+10**(d//2)-1)
    U = S[::-1]
    T = S + U[1:]

print(T)


