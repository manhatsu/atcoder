N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

remA = [0]*46
remB = [0]*46
remC = [0]*46

for i in range(N):
    remA[A[i]%46]+=1
    remB[B[i]%46]+=1
    remC[C[i]%46]+=1

D = []
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k) % 46 == 0:
                D.append((i, j, k))

ans = 0
for (i, j, k) in D:
    ans += remA[i]*remB[j]*remC[k]

print(ans)




