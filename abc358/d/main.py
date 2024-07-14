N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

i = 0
j = 0

C = []
ret = True
while (i < N) and (j < M):
    while (B[j] > A[i]):
        i += 1
        if i >= N:
            ret = False
            break
    if ret == False:
        break
    C.append(A[i])
    i += 1
    j += 1

print(sum(C) if len(C) == M else -1)

    



