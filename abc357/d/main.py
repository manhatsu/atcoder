MOD = 998244353


N = int(input())
d = len(str(N))
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))


# N*(10^0+10^d+10^2d+.......+10^(N-1)d)
#        10^dN - 1
# = N * ----------
#        10^d - 1

ret1 = N%MOD

ret2 = (pow(10, d*N, MOD) - 1)%MOD

ret3 = pow((pow(10, d, MOD) - 1), MOD-2, MOD)

print(ret1*ret2%MOD*ret3%MOD)












