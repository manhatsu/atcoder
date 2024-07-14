H, W = map(int, input().split())

F = [[] for _ in range(H)]

for i in range(H):
    A_list = list(map(int, input().split()))
    F[i] += A_list

SH = [0]*H
SW = [0]*W

for i in range(H):
    for j in range(W):
        SH[i] += F[i][j]
        SW[j] += F[i][j]

B = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        B[i][j] = SH[i]+SW[j]-F[i][j]

for i in range(H):
    print(*B[i])








