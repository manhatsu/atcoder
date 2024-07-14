N, M = map(int, input().split())

ls = [0]*(N+1)
ls[0] = -1

for j in range(M):
    a, b = map(int, input().split())
    ls[b] = 1


strong_idx = [i for i, x in enumerate(ls) if x == 0]
if len(strong_idx) == 1:
    print(strong_idx[0])
else:
    print(-1)



