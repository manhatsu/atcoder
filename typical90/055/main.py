N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
'''
remA = [a % P for a in A]

from itertools import combinations
base = list(combinations(remA, 5))
ans = 0
for B in base:
    pie = 1
    for b in B:
            pie *= b
    if pie % P == Q:
        ans += 1
'''
# 上だとTLEする

ans = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    if A[i]%P*A[j]%P*A[k]%P*A[l]%P*A[m]%P == Q:
                        ans += 1

print(ans)



