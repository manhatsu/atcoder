import math

L, R = map(int, input().split())
# A_list = list(map(int, input().split()))

MOD = 10**9+7

# log10だと15.6桁以上で精度が足りない
# l = int(math.log10(L))+1
# r = int(math.log10(R))+1
l = len(str(L))
r = len(str(R))

temp = 0
if l == r:
    temp = (L+R)*(R+1-L)*l//2

else:  
    # l桁
    temp += (L+10**l-1)*(10**l-L)*l//2
    # l+1 ~ r-1 桁
    if r > l+1:
        for i in range(l+1, r):
            temp += (10**(i-1)+10**i-1)*(10**i-10**(i-1))*i//2
    # r桁
    temp += (10**(r-1)+R)*(R+1-10**(r-1))*r//2

print(temp % MOD)

# 逆元のMODはpowで取れる．







