from collections import deque
N, M = map(int, input().split())

INF = float("inf")

G = [[] for i in range(N)]
for i in range(M):
    a, b, x, y = map(int, input().split())
    a, b = a-1, b-1
    G[a].append((b, x, y))
    G[b].append((a, -x, -y))

seen = [(INF, INF)] * N

seen[0] = (0, 0)
Q = deque()
Q.append(0)

while Q:
    q = Q.popleft()
    for (lq, lx, ly) in G[q]:
        if seen[lq] != (INF, INF):
            continue
        seen[lq] = (seen[q][0]+lx, seen[q][1]+ly)
        Q.append(lq)

for i in range(N):
    if seen[i] == (INF, INF):
        print('undecidable')
    else:
        print(*seen[i])


