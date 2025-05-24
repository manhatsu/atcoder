import heapq
N, M = map(int, input().split())
# A_list = list(map(int, input().split()))
INF = float('inf')

F = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    F[a-1].append((c, b-1))
    F[b-1].append((c, a-1))

dist0 = [INF]*N

L = []
dist0[0] = 0
heapq.heapify(L)
heapq.heappush(L, (0, 0))

while len(L) > 0:
    c, v = heapq.heappop(L)
    if dist0[v] < c:
        continue
    for nc, nv in F[v]:
        if dist0[nv] > dist0[v]+nc:
            dist0[nv] = dist0[v]+nc
            heapq.heappush(L, (dist0[nv], nv))

dist1 = [INF]*N

L = []
dist1[N-1] = 0
nv = N-1
heapq.heapify(L)
heapq.heappush(L, (0, N-1))

while len(L) > 0:
    c, v = heapq.heappop(L)
    if dist1[v] < c:
        continue
    for nc, nv in F[v]:
        if dist1[nv] > dist1[v]+nc:
            dist1[nv] = dist1[v]+nc
            heapq.heappush(L, (dist1[nv], nv))

for i in range(N):
    print(dist0[i]+dist1[i])
    





