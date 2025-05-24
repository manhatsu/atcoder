# コストの小さい順に、A[0]に対して各点が連結でないならmergeしていけば良い

from atcoder.dsu import DSU

N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

U = DSU(N)

Q = []
for i in range(M):
    k, c = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    Q.append((c, A))

Q = sorted(Q)
cost = 0
for c, A in Q:
    for a in A[1:]:
        if not U.same(A[0], a):
            U.merge(A[0], a)
            cost += c

for i in range(1, N):
    if not U.same(0, i):
        cost = -1

print(cost)