from calendar import c
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

N, K = map(int, input().split())
# A = list(map(int, input().split()))

S = input()
T = []
for i in range(len(S)):
    if S[i] == 'o':
        T.append('o')
    elif S[i] == '.':
        T.append('.')
    else:        
        if i == 0:
            if i+1 < len(S) and S[i+1] == 'o':
                T.append('.')
            else:
                T.append('?')
        elif i == len(S) - 1:
            if S[i-1] == 'o':
                T.append('.')
            else:
                T.append('?')
        else:
            if S[i-1] == 'o' or S[i+1] == 'o':
                T.append('.')
            else:
                T.append('?')

ans_temp = ''.join(T)

can_change = 0
temp_ques = 0
for a in ans_temp:
    if a == '?':
        temp_ques += 1
    else:
        if temp_ques % 2 != 0:
            can_change += temp_ques // 2 + 1
        else:
            can_change += temp_ques // 2
        temp_ques = 0
if temp_ques % 2 != 0:
    can_change += temp_ques // 2 + 1
else:
    can_change += temp_ques // 2

if K == ans_temp.count('o'):
    ans = ''.join(T)
    ans = ans.replace('?', '.')
else:
    if can_change <= K - ans_temp.count('o'):
        temp_ques = 0
        for i, a in enumerate(ans_temp):
            if a == '?':
                temp_ques += 1
            else:
                if temp_ques % 2 != 0:
                    for j in range(temp_ques // 2 + 1):
                        T[i - 1 - 2*j] = 'o'
                    for k in range(temp_ques // 2):
                        T[i - 2 - 2*k] = '.'
                temp_ques = 0
        if temp_ques % 2 != 0:
            for j in range(temp_ques // 2 + 1):
                T[-1 - 2*j] = 'o'
            for k in range(temp_ques // 2):
                T[-2 - 2*k] = '.'          
    ans = ''.join(T)
print(ans)
    






