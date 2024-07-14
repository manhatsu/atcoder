N, Q = map(int, input().split())
A = list(map(int, input().split()))

aida = [A[i+1] - A[i] for i in range(len(A)-1)]

fuben = sum([abs(a) for a in aida])

for i in range(Q):
    L, R, V = map(int, input().split())
    L = L-1
    R = R-1
    if L >= 1:
        fuben -= abs(aida[L-1])
        aida[L-1] += V
        fuben += abs(aida[L-1])
    if R < N-1:
        fuben -= abs(aida[R])
        aida[R] -= V
        fuben += abs(aida[R])
    print(fuben)





