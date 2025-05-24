
from bisect import bisect_left, bisect_right
N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]
B = sorted(list(map(int, input().split())))[::-1]

i, j = 0, 0

ans = -1
while i < N and j < M:
    if abs(A[i]-B[j]) <= D:
        ans = A[i]+B[j]
        break
    if A[i] < B[j]:
        j += 1
        continue
    else:
        i += 1
        continue

print(ans)
    


