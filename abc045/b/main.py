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

A = list(input())
B = list(input())
C = list(input())

D = []
D.append(deque(A))
D.append(deque(B))
D.append(deque(C))

now = 0
dic = {'a':0, 'b':1, 'c':2}
while True:
    if not D[now]:
        break
    l = D[now].popleft()
    now = dic[l]

if now == 0:
    print('A')
elif now == 1:
    print('B')
else:
    print('C')

