N = int(input())

C1 = [0]
C2 = [0]

for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        C1.append(p)
        C2.append(0)
    else:
        C2.append(p)
        C1.append(0)

# 累積和
import itertools

S1 = list(itertools.accumulate(C1))
S2 = list(itertools.accumulate(C2))

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    ret1 = S1[r]-S1[l-1]
    ret2 = S2[r]-S2[l-1]
    print(ret1, ret2)






