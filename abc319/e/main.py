
N, X, Y = map(int, input().split())

P = []
T = [] 

for _ in range(N-1):
    p, t = map(int, input().split())
    P.append(p)
    T.append(t)

B = [0]*840

for t in range(840):
    now = t
    for i in range(N-1):
        rem = now % P[i]
        towait = 0 if rem == 0 else P[i] - rem
        now += towait + T[i]
    B[t] = now - t

Q = int(input())
for _ in range(Q):
    q = int(input())
    ans = q + X + B[(q+X)%840] + Y
    print(ans)
