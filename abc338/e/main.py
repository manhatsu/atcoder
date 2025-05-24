from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from shutil import which
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

which_line_dict = dict()
formers = set()
latters = set()
for i in range(N):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    which_line_dict[a] = i
    which_line_dict[b] = i
    formers.add(min(a, b))
    latters.add(max(a, b))

flag = True
S = []   
for i in range(2*N):
    if i in formers:
        S.append(which_line_dict[i])
    else:
        if len(S) == 0:
            flag = False
            break
        j = S.pop()
        if j != which_line_dict[i]:
            flag = False
            break

print('No' if flag else 'Yes')


