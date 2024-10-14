Q = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
MOD = 998244353
from collections import deque

S = deque()
S.append(1)
T = 1
    

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        T = (T*10+q[1])%MOD
        S.append(q[1])
    elif q[0] == 2:
        s = S.popleft()
        T -= s*pow(10, len(S), MOD)%MOD
    else:
        T %= MOD
        print(T)




