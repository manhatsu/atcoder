import sys
sys.setrecursionlimit(10**8)

N = int(input())
A = list(map(int, input().split()))
A = [a-1 for a in A]

from collections import deque

seen = [0]*N

def search(idx, Q):
    # print('search', idx)
    if seen[idx] != 0:
        return idx
    else:
        seen[idx] = 1
        Q.append(idx)
        return search(A[idx], Q)

Q = deque()
idx = search(0, Q)
# print(Q)
# print(idx)
while Q:
    q = Q.popleft()
    if q == idx:
        Q.appendleft(idx)
        break

ans = list(Q)
# print(ans)
print(len(ans))
ans = [a+1 for a in ans]
print(*ans)

        






