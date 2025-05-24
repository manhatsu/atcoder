from collections import defaultdict, deque
# from itertools import combinations, permutations
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
M = math.ceil(math.log2(N))
print(M)

L = [[] for i in range(M)]
for i in range(M):
    for j in range(N):
        if j >> i & 1:
            L[i].append(j)

for i in range(M):
    print(len(L[i]), *[l+1 for l in L[i]])

S = input()
ans = set([i for i in range(N)])
# print(ans)
for i, s in enumerate(S):
    if int(s) == 1:
        ans &= set(L[i])
    else:
        ans -= set(L[i])
    # print(ans)

print(list(ans)[0]+1)


'''
span = N
prev_todrink = [1]*N
L = []
for i in range(M):
    # print('person', i)
    j = 0
    temp = []
    todrink = [-1]*N
    while True:
        if j == N:
            # print('reached end')
            # print(*temp)
            for k in temp[0:math.ceil(len(temp)/2)]:
                # print('drink', k)
                todrink[k] = 1
            for k in temp[math.ceil(len(temp)/2):]:
                # print('do not drink', k)
                todrink[k] = 0
            break
        if len(temp) == 0 or prev_todrink[temp[-1]] == prev_todrink[j]:
            temp.append(j)
            j += 1
            continue
        # print(*temp)
        for k in temp[0:math.ceil(len(temp)/2)]:
            # print('drink', k)
            todrink[k] = 1
        for k in temp[math.ceil(len(temp)/2):]:
            # print('do not drink', k)
            todrink[k] = 0
        temp = []
        continue
    L.append(todrink)
    prev_todrink = todrink

for i in range(M):
    drink_number = [j+1 for j in range(N) if L[i][j] == 1]
    print(len(drink_number), *drink_number)

L = [''.join([str(m) for m in l]) for l in L]
# print(*L)
L = [int(l, 2) for l in L]
# print(*L)

S = input()

ans_bit = 2**N-1
# print(bin(ans_bit))
for i, s in enumerate(S):
    if int(s) == 1:
        ans_bit &= L[i]
    else:
        ans_bit &= ~L[i]

# print(bin(ans_bit))
ans = 0
while True:
    if ans_bit >> ans & 1:
        break
    ans += 1
ans = N - ans
print(ans)
'''






    


