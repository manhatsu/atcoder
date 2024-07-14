# N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = True
for i in range(3):
    if (A[i]<B[i+3] and A[i+3]>B[i]) or (B[i]<A[i+3] and B[i+3]>A[i]):
        continue
    else:
        ans = False
        break

print('Yes' if ans else 'No')




