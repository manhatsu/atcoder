from sortedcontainers import SortedDict, SortedList, SortedSet
N = int(input())
Q = int(input())

# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

B = [[] for i in range(N+1)]
C = [set() for i in range(2*10**5+1)]

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        B[q[2]].append(q[1])
        C[q[1]].add(q[2])

    elif q[0] == 2:
        b = B[q[1]].copy()
        b = SortedList(b)
        print(*b)
    else:
        c = C[q[1]].copy()
        c = SortedSet(c)
        print(*c)



