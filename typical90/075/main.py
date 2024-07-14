import math

N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

def prime_factorization(N):
    a = []
    while (N >= 2 and N % 2 == 0):
        N /= 2
        a.append(2)
    q = 3
    for i in range(int(q), int(N ** 0.5)+1, 2):
        # print(i)
        while (N % i == 0):
            N /= i
            a.append(i)
    if N > 1:
        a.append(N)

    return a

a = prime_factorization(N)
# print(a)

print(math.ceil(math.log2(len(a))))



