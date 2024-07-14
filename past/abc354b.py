N = int(input())

S = []
C = []
for _ in range(N):
    L = list(input().split())
    s = L[0]
    c = int(L[1])
    S.append(s)
    C.append(c)

sorted_S = sorted(S)

T = sum(C)

idx = T % N

print(sorted_S[idx])
