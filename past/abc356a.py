N, L, R = map(int, input().split())

ret1 = [i for i in range(1, L)]
ret2 = [i for i in range(L, R+1)][::-1]
ret3 = [i for i in range(R+1, N+1)]

ret = ret1+ret2+ret3

print(*ret)