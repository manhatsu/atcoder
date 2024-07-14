N = int(input())

F = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    F[a-1].append(b-1)
    F[b-1].append(a-1)

# print(F)

from collections import deque

seen = [0]*N
dist = [0]*N

def bfs(start, F, seen, dist):
    Q = deque()
    Q.append(start)

    while Q:
        now = Q.popleft()
        seen[now] = 1
        for nex in F[now]:
            if not seen[nex]:
                Q.append(nex)
                dist[nex] = dist[now]+1

    return

bfs(0, F, seen, dist)
maxd = max(dist)
start = dist.index(maxd)

seen1 = [0]*N
dist1 = [0]*N

bfs(start, F, seen1, dist1)

print(max(dist1)+1)