N, M = map(int, input().split())

ret = 0
for i in range(len(str(bin(M)))-2):
    if ((M >> i) & 1):
        # print(i, 'shift')
        shou = (N+1) // (2**(i+1))
        amari = (N+1) % (2**(i+1))
        # print(shou, amari)

        ret += shou * 2 ** i
        ret += max(amari-2**i, 0)
        # print('ret', ret)

print(ret % 998244353)

