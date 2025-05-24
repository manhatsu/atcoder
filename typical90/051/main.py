from sortedcontainers import SortedList

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

B = A[:N//2]
C = A[N//2:]

Bsum = [[] for _ in range(len(B)+1)]
Csum = [SortedList() for _ in range(len(C)+1)]

for i in range(2**len(B)):
    k = i.bit_count()
    s = 0
    for j in range(len(B)):
        if i >> j & 1:
            s += B[j]
    Bsum[k].append(s)

for i in range(2**len(C)):
    k = i.bit_count()
    s = 0
    for j in range(len(C)):
        if i >> j & 1:
            s += C[j]
    Csum[k].add(s)

ans = 0
for i in range(len(Bsum)):
    if K-i < 0 or K-i >= len(Csum):
        continue
    for b in Bsum[i]:
        ans += Csum[K-i].bisect_right(P-b)

print(ans)

