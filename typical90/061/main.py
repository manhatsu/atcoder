Q = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
shift = 0
U = []
D = []

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        U.append(x)
    elif t == 2:
        D.append(x) 
    else:
        if len(U) >= x:
            print(U[len(U)-x])
            # U[::-1]すると間に合わない O(N)だから．
        else:
            print(D[x-1-len(U)])

        






