N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

F = []

for i in range(N):
    S = input()
    F.append(S)

# print(F)

ret = N
for i in range(2**N):
    # print(bin(i))
    popc = [0]*M
    nshops = 0
    for j in range(N):
        if ((i >> j) & 1):
            # print('visit shop {}'.format(j))
            nshops += 1
            for k, s in enumerate(F[j]):
                # print('s', s)
                if s == 'o':
                    # print('s == o')
                    popc[k] = 1
                # print(popc)
    if sum(popc) == M:
        ret = min(ret, nshops)

print(ret)
