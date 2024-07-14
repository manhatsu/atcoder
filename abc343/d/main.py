N, T = map(int, input().split())
# A_list = list(map(int, input().split()))

S = [0]*N
D = {0:N}
ret = 1

for _ in range(T):
    a, b = map(int, input().split())
    a -= 1
    D[S[a]] -= 1
    if D[S[a]] == 0:
        del D[S[a]]
        ret -= 1
    S[a] += b
    if not S[a] in D.keys():
        D[S[a]] = 1
        ret += 1
    else:
        D[S[a]] += 1
    print(ret)

