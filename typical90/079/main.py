H, W = map(int, input().split())
# A_list = list(map(int, input().split()))

A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

B = []
for _ in range(H):
    B.append(list(map(int, input().split())))

dh = [0, 0, 1, 1]
dw = [0, 1, 0, 1]

ret = True
kaisuu = 0
for h in range(H-1):
    for w in range(W-1):
        diff = A[h][w] - B[h][w]
        if (diff != 0):
            kaisuu += abs(diff)
            for i in range(4):
                nh = h + dh[i]
                nw = w + dw[i]
                A[nh][nw] -= diff
    if A[h][W-1] != B[h][W-1]:
        ret = False
        break
    if not ret:
        break

for j in range(W):
    if A[H-1][j] != B[H-1][j]:
        ret = False
        break

if ret:
    print('Yes')
    print(kaisuu)
else:
    print('No')