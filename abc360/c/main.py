N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

B = [[] for i in range(N+1)]

for i in range(N):
    B[A[i]].append(W[i])

import heapq
cost = 0
for b in B:
    L = len(b)
    if L > 1:
        heapq.heapify(b)
        for i in range(L-1):
            cost += heapq.heappop(b)

print(cost)









