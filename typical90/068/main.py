from atcoder.dsu import DSU

N = int(input())
Q = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

if N == 1:
    for _ in range(Q):
        t, x, y, v = map(int, input().split())
        if t == 1:
            print(v)

    exit()

S = [-1]*(N-1)
cand_val = [0]*N

U = DSU(N)

T1 = []

for _ in range(Q):
    t, x, y, v = map(int, input().split())
    x, y = x-1, y-1
    if t == 0:
        U.merge(x, y)
        S[x] = v
    else:
        if U.same(x, y):
            T1.append((x, y, v))
        else:
            T1.append((-1, -1, -1))


for i in range(1, N):
    if S[i-1] == -1:
        cand_val[i] = 0
    else:
        cand_val[i] = S[i-1] - cand_val[i-1]

for x, y, v in T1:
    if x == -1:
        print("Ambiguous")
    else:
        if (y-x)%2 == 0:
            print(cand_val[y] + v - cand_val[x])
        else:
            print(cand_val[y] - v + cand_val[x])