from collections import deque
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
G = [[] for i in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [0]*(N+1)
dist = [-1]*(N+1)

Q = deque()
Q.append(1)
dist[1] = 0

while Q:
    now = Q.popleft()
    for lidx in G[now]:
        if dist[lidx] != -1:
            continue
        dist[lidx] = dist[now]+1
        Q.append(lidx)

# print(dist)

E = []
O = []
for i, d in enumerate(dist):
    if i == 0:
        continue
    if d % 2 == 0:
        E.append(i)
    else:
        O.append(i)

if len(E) >= (N // 2):
    print(*E[:N//2])
else:
    print(*O[:N//2])

# 木は2部グラフなので，2色で塗り分ける事を考える
# 片方の色の頂点は必ずN/2個以上あるので，そこからN/2個選んで出力すれば良い

