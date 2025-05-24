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
from icecream import ic

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

dp0 = {int('1'*(i+1)):'1'*(i+1) for i in range(4)} # かっこ不要
dp1 = {int('1'*(i+1)):'' for i in range(4)}
for i in range(2, N+1):
    ret_plus = ''
    ret_multiply = ''
    if i in dp0:
        ret_plus = dp0[i]
    if i in dp1:
        ret_multiply = dp1[i]

    for j in range(1, i):
        k = i-j
        if len(dp0[j]) > 0 and len(dp1[j]) > 0:
            temp0 = dp0[j] if len(dp0[j]) <= len(dp1[j]) else dp1[j]
        elif len(dp0[j]) > 0:
            temp0 = dp0[j]
        else:
            temp0 = dp1[j]
        if len(dp0[k]) > 0 and len(dp1[k]) > 0:
            temp1 = dp0[k] if len(dp0[k]) <= len(dp1[k]) else dp1[k]
        elif len(dp0[k]) > 0:
            temp1 = dp0[k]
        else:
            temp1 = dp1[j]
        temp = temp0 + '+' + temp1
        if len(ret_plus) == 0 or len(temp) < len(ret_plus):
            ret_plus = temp

    for j in range(2, i):
        if i % j != 0:
            continue
        k = i // j
        if len(dp0[j]) > 0 and len(dp1[j]) > 0:
            temp0 = ('(' + dp1[j] + ')') if (len(dp1[j]) + 2) < len(dp0[j]) else dp0[j]
        elif len(dp0[j]) > 0:
            temp0 = dp0[j]
        else:
            temp0 = '(' + dp1[j] + ')'
        if len(dp0[k]) > 0 and len(dp1[k]) > 0:
            temp1 = ('(' + dp1[k] + ')') if (len(dp1[k]) + 2) < len(dp0[k]) else dp0[k]
        elif len(dp0[k]) > 0:
            temp1 = dp0[k]
        else:
            temp1 = '(' + dp1[k] + ')'
        temp = temp0 + '*' + temp1
        if len(ret_multiply) == 0 or len(temp) < len(ret_multiply):
            ret_multiply = temp

    dp0[i] = ret_multiply
    dp1[i] = ret_plus
        
if len(dp0[N]) == 0:
    print(dp1[N])
elif len(dp1[N]) == 0:
    print(dp0[N])
else:
    print(dp0[N] if len(dp0[N]) <= len(dp1[N]) else dp1[N])

