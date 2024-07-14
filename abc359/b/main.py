
N = int(input())
A = list(map(int, input().split()))

ret = 0
for i in range(2*N-2):
    if A[i] == A[i+2]:
        ret += 1

print(ret)




