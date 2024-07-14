N = int(input())
A = list(map(int, input().split()))

MOD = 998244353

# Aの総和
S = []
# 10^dの総和
E = []

temp_s = 0
temp_e = 0

for a in A:
    temp_s += a
    S.append(temp_s%MOD)
    d = len(str(a))
    temp_e += pow(10, d, MOD)
    E.append(temp_e%MOD)

ret1 = 0
ret2 = 0
for i in range(N-1):
    ret1 += A[i]*(E[N-1]-E[i])%MOD
    ret2 += (S[N-1]-S[i])%MOD

print((ret1+ret2)%MOD)


    







