from collections import deque, defaultdict
from math import e
N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

G = [defaultdict(int) for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    if a == b:
        G[a][b] += 1
        continue
    G[a][b] += 1
    G[b][a] += 1

# print('G:', G)

seen = [0]*N

for i in range(N):
    if seen[i]:
        continue
    points = set([i])
    edges = dict()
    Q = deque([i])

    while Q:
        q = Q.popleft()
        seen[q] = 1
        for lq, val in G[q].items():
            if lq > q:
                if (q, lq) not in edges:
                    edges[(q, lq)] = val
            else:
                if (lq, q) not in edges:
                    edges[(lq, q)] = val
            if lq not in points:
                points.add(lq)
                Q.append(lq)
    # print('points:', points)
    # print('edges:', edges)
    sum_edges = sum([val for val in edges.values()])
    if len(points) != sum_edges:
        print('No')
        exit()


print('Yes')
    




