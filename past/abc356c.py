N, M, K = map(int, input().split())

C = []
A = []
R = []

for _ in range(M):
    temp = list(input().split())
    c = int(temp[0])
    C.append(c)
    a_list = sorted([int(t) for t in temp[1:-1]])
    A.append(a_list)
    r = temp[-1]
    R.append(r)

# print(A)

ans = 0
for i in range(2**N):
    ret = True
    for j, a_list in enumerate(A):
        keynum = 0
        for a in a_list:
            if ((i >> (a-1)) & 1):
                keynum += 1
        if (keynum < K) and (R[j] == 'o'):
            ret = False
            break
        if (keynum >= K) and (R[j] == 'x'):
            ret = False
            break
        if not ret:
            break
    if ret:
        ans += 1

print(ans)
