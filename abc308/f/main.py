import bisect
# from icecream import # ic
import heapq


N, M = map(int, input().split())
P = list(map(int, input().split()))
L = list(map(int, input().split()))
D = list(map(int, input().split()))

P = sorted(P)
Z = zip(L, D)
Z = sorted(Z, key=lambda x: x[0])
L, D = zip(*Z)

L = list(L)
D = list(D)

# ic(P)
# ic(L)
# ic(D)



K = []
for l in L:
    invk = bisect.bisect_left(P, l)
    k = len(P)-invk
    K.append(k)

# ic(K)

touse = []
heapq.heapify(touse)

while len(K) > 0:
    k = K.pop()
    heapq.heappush(touse, D.pop())

    while len(touse) > k:
        heapq.heappop(touse)

# ic(touse)

ans = sum(P) - sum(touse)

print(ans)







