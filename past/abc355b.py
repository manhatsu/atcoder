N, M = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

flag = False

C = []
a = 0
b = 0

prev = -1

ret = False
while (a < N and b < M):
    if A[a] < B[b]:
        # print(A[a])
        if prev == 0:
            ret = True
            break
        a += 1
        prev = 0
    else:
        # print(B[b])
        b = b+1
        prev = 1

if b == M:
    if a <= N-2:
        ret = True

print('Yes' if ret else 'No')

