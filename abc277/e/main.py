from calendar import c
from collections import deque

N, M, K = map(int, input().split())
# A_list = list(map(int, input().split()))

G0 = [set() for _ in range(N)]
G1 = [set() for _ in range(N)]

for _ in range(M):
    u, v, a = map(int, input().split())
    u, v = u-1, v-1
    if a == 0:
        G0[u].add(v)
        G0[v].add(u)
    else:
        G1[u].add(v)
        G1[v].add(u)

S = set()
if K > 0:
    temp = list(map(int, input().split()))
    S = set([t-1 for t in temp])

seen0 = [0]*N
seen1 = [0]*N

seen1[0] = 1
Q = deque()
Q.append((0, 0, 1)) # node, cost, status
if 0 in S:
    seen0[0] = 1
    Q.append((0, 0, 0))

ans = -1
while Q:
    n, c, s = Q.popleft()
    if n == N-1:
        ans = c
        break
    if s == 0:
        for nn in G0[n]:
            if not seen0[nn]:
                seen0[nn] = 1
                Q.append((nn, c+1, 0))
            if nn in S and not seen1[nn]:
                seen1[nn] = 1
                Q.append((nn, c+1, 1))
    else:
        for nn in G1[n]:
            if not seen1[nn]:
                seen1[nn] = 1
                Q.append((nn, c+1, 1))
            if nn in S and not seen0[nn]:
                seen0[nn] = 1
                Q.append((nn, c+1, 0))

print(ans)