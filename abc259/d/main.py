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

N = int(input())
sx, sy, tx, ty = map(int, input().split())
C = []
for i in range(N):
    x, y, r = map(int, input().split())
    C.append((x, y, r))

G = [[] for i in range(N)]

start_circle = []
end_circle = set()

for i in range(N):
    x0, y0, r0 = C[i]
    if (sx-x0)**2+(sy-y0)**2 == r0**2:
        start_circle.append(i)
    if (tx-x0)**2+(ty-y0)**2 == r0**2:
        end_circle.add(i)

flag = False
if N == 1:
    if 0 in start_circle:
        if 0 in end_circle:
            flag = True

else:
    for i in range(N-1):
        for j in range(i+1, N):
            x0, y0, r0 = C[i]
            x1, y1, r1 = C[j]

            dist = (x0-x1)**2 + (y0-y1)**2
            if dist < (r0-r1)**2:
                continue
            if dist <= (r0+r1)**2 and dist >= (r0-r1)**2:
                G[i].append(j)
                G[j].append(i)

    seen = [0]*N

    for s in start_circle:
        if seen[s] != 0:
            continue
        if s in end_circle:
            flag = True
            break
        seen[s] = 1
        Q = deque()
        Q.append(s)
        
        while Q:
            q = Q.popleft()
            for lq in G[q]:
                if seen[lq] != 0:
                    continue
                if lq in end_circle:
                    flag = True
                    break
                seen[lq] = 1
                Q.append(lq)
            if flag:
                break

        if flag:
            break

print('Yes' if flag else 'No')




