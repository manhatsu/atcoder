N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

C = [b-a for a, b in zip(A, B)]
# print(C)

print(sum(A)+max(C))
