N, M = map(int, input().split())

S = []
for i in range(N):
    s = input()
    S.append(s)

from itertools import permutations

perm = list(permutations([i for i in range(N)]))

ret = True
for P in perm:
    ret = True
    for i in range(N-1):
        count = 0
        for j in range(M):
            if S[P[i]][j] != S[P[i+1]][j]:
                count += 1
                if count > 1:
                    break
        # print('diff for {} and {}'.format(P[i], P[i+1]), count)
        if (count == 0) or (count > 1):
            ret = False
            break
    if ret:
        # print(P)
        break

print('Yes' if ret else 'No')