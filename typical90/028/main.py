N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

F = [[0]*1001 for _ in range(1001)]

for i in range(N):
    # print('loop', i)
    lx, ly, rx, ry = map(int, input().split())
    # print(lx, ly, rx, ry)
    F[lx][ly] += 1
    # print(F[lx][ly])
    # if (rx+1) <= 1000:
    F[rx][ly] -= 1
    # if (ry+1) <= 1000:
    F[lx][ry] -= 1
    # if ((rx+1) <= 1000) and ((ry+1) <= 1000):
    F[rx][ry] += 1

for i in range(1001):
    for j in range(1, 1001):
        F[i][j] += F[i][j-1]

for i in range(1, 1001):
    for j in range(1001):
        F[i][j] += F[i-1][j]

M = [0]*(N+1)

for i in range(1001):
    for j in range(1001):
        # if F[i][j] != 0:
            # print('i, j, F[i][j]', i, j, F[i][j])
        M[F[i][j]] += 1

for i in range(1, N+1):
    print(M[i])

# 2次元いもす法

