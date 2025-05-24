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

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

stack = []
for i in range(M):
    stack.append((X[i]-1, A[i]))

stack = sorted(stack)
# print(stack)

ret = True
j = N-1
ans = 0
while len(stack) > 0:
    i, v = stack.pop()
    if i > j:
        ret = False
        break
    if i == j:
        if v == 1:
            j -= 1
            continue
        else:
            ret = False
            break
    if v > j-i+1:
        ret = False
        break
    if v == j-i+1:
        ans += ((j-i)+1)*(v-1)//2
        j = i-1
    else:
        ans += ((j-i)+(j-i-(v-1)))*v//2
        j -= v

if ret and j == -1:
    print(ans)
else:
    print(-1)
