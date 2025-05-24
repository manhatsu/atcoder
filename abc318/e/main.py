
N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0]*(3*10**5+1)
C = [0]*(3*10**5+1)
last_idx = [-1]*(3*10**5+1)
count = [0]*(3*10**5+1)

for i in range(N):
    if last_idx[A[i]] == -1:
        last_idx[A[i]] = i
        count[A[i]] += 1
        continue
    B[A[i]] += (i-last_idx[A[i]]-1)*count[A[i]]
    C[A[i]] += B[A[i]]
    
    last_idx[A[i]] = i
    count[A[i]] += 1

# print(*B[:15])
# print(*C[:15])

ans = 0
for c in C:
    ans += c

print(ans)