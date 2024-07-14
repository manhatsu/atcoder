N, K = map(int, input().split())
P = list(map(int, input().split()))
IDX = [i for i in range(N)]

zip_s = sorted(zip(P, IDX))
_, IDX = zip(*zip_s)

from sortedcontainers import SortedSet, SortedList
# 平衡二分探索木

ss = SortedSet(IDX[0:K])
ans = ss[-1]-ss[0]
for i in range(N-K):
    ss.discard(IDX[i])
    ss.add(IDX[i+K])
    ans = min(ans, ss[-1]-ss[0])

print(ans)






