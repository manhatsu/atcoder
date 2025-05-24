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

S = input()
K = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

Q = deque()

ans = 0
left = 0
for i in range(len(S)):
    if S[i] == 'X':
        continue
    if len(Q) < K:
        Q.append(i)
    else:
        if K == 0:
            ans = max(ans, i-left)
            left = i+1
        else:
            ans = max(ans, i-left)
            left = Q.popleft()+1
            Q.append(i)

ans = max(ans, len(S)-left)
print(ans)

        