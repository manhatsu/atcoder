import heapq
from sortedcontainers import SortedList

N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

ans = [0]*N

L = SortedList([i for i in range(N)])
R = SortedList([]) # time, idxで入れる

for i in range(M):
    t, w, s = map(int, input().split())
    while len(R) > 0 and t >= R[0][0]:
        _, idx = R.pop(0)
        L.add(idx)
    if len(L) > 0:
        l = L.pop(0)
        ans[l] += w
        R.add((t+s, l))

for i in range(N):
    print(ans[i])