N, M = map(int, input().split())

S = [0]*M

A_list = list(map(int, input().split()))

for _ in range(N):
    X_list = list(map(int, input().split()))
    for i in range(M):
        A_list[i] -= X_list[i]

if any([a > 0 for a in A_list]):
    print('No')
else:
    print('Yes')

