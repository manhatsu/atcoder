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

N, M = map(int, input().split())
P = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(1, N):
    G[P[i-1]-1].append(i)

insurances = [-1]*N

for i in range(M):
    x, y = map(int, input().split())
    x = x-1
    insurances[x] = max(y, insurances[x])

# print(*insurances)
isCovered = [i != -1 for i in insurances]

Q = deque()

if insurances[0] == -1:
    Q.append((0, -1))
else:
    isCovered[0]
    Q.append((0, insurances[0]-1))
while Q:
    q, r = Q.popleft()
    for lq in G[q]:
        insurances[lq] = max(r, insurances[lq])
        if insurances[lq] == -1:
            Q.append((lq, -1))
        else:
            isCovered[lq] = True
            Q.append((lq, insurances[lq]-1))

print(sum(isCovered))
# print(*isCovered)


