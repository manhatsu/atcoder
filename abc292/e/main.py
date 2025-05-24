from collections import deque

N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

G = [[] for _ in range(N)]

already_connected_edges = 0
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    already_connected_edges += 1

all_edges = 0

for i in range(N):
    seen = [0]*N

    Q = deque()
    Q.append(i)
    seen[i] = 1
    
    while Q:
        v = Q.popleft()
        for nv in G[v]:
            if seen[nv]:
                continue
            all_edges += 1
            seen[nv] = 1
            Q.append(nv)

print(all_edges - already_connected_edges)






