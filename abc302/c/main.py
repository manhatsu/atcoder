N, M = map(int, input().split())

from itertools import permutations

S = []
for i in range(N):
    S.append(input())

perm = list(permutations(S))

ans = 'No'
for P in perm:
    ret = True
    for i in range(N-1):
        diff = 0
        for j in range(M):
            if P[i][j] != P[i+1][j]:
                diff += 1
        if diff != 1:
            ret = False
            break
    if not ret:
        continue
    ans = 'Yes'
    break

print(ans)
    
        
