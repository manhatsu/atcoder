N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

D = sum([abs(a-b) for a, b in zip(A, B)])

if ((K-D) >= 0) and ((K-D) % 2 == 0):
    print('Yes')
else:
    print('No')






