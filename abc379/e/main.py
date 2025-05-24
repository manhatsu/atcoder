from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# sys.set_int_max_str_digits(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
S = input()

I = [0]*N

for i, s in enumerate(S):
    if i == 0:
        I[0] += int(s)
        continue
    I[0] += int(s)*(i+1)
    I[N-i] -= int(s)*(i+1)

temp = 0
A = []
for i in range(N):
    temp += I[i]
    A.append(temp)

A.append(0)

# print(*A)

ans = ''
for i in range(len(A)-1):
    r = A[i] % 10
    q = A[i] // 10
    ans += str(r)
    A[i+1] += q

last = A[-1]
while last > 0:
    r = A[-1] % 10
    q = A[-1] // 10
    ans += str(r)
    last = q

ans = ans[::-1]

print(ans)
