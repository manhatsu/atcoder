from bisect import bisect_left

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

LIS = [A[0]]
m0 = [1]
for a in A[1:]:
    if a > LIS[-1]:
        LIS.append(a)
    else:
        LIS[bisect_left(LIS, a)] = a
    m0.append(len(LIS))

ILIS = [A[-1]]
m1 = [1]
for a in A[-2::-1]:
    if a > ILIS[-1]:
        ILIS.append(a)
    else:
        ILIS[bisect_left(ILIS, a)] = a
    m1.append(len(ILIS))

ans = 0
for i in range(N):
    ans = max(ans, m0[i]+m1[N-1-i]-1)

print(ans)




