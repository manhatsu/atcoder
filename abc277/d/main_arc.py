from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
S = sum(A)

B = A+A
# print(B)

i, j = 0, 0
inv_ret = 0
while i < N:
    temp = B[j]
    prev = B[j]
    j += 1
    while j < N+i:
        if B[j]%M == prev%M or B[j]%M == (prev+1)%M:
            temp += B[j]
            prev = B[j]
            j += 1
            continue
        break
    if temp > inv_ret:
        inv_ret = temp
    i = j

print(S-inv_ret)






