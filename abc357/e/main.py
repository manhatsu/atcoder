from collections import deque
N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a-1 for a in A]

F = [[] for i in range(N)]
for i in range(N):
    F[A[i]].append(i)

# print(F)

seen = [0]*N
ans = 0
toadd = [0]*N

for i in range(N):
    if seen[i]:
        continue
    stack = [i]
    now = i
    seen[i] = 1

    while True:
        now = A[now]
        if seen[now]:
            break
        seen[now] = 1
        stack.append(now)

    cycle = [now]
    while True:
        v = stack.pop()
        if v == now:
            break
        cycle.append(v)

    # print(cycle)

    ans += len(cycle)*len(cycle)

    set_cycle = set(cycle)
    for v in cycle:
        Q = deque()
        Q.append(v)
        while Q:
            q = Q.popleft()
            for lq in F[q]:
                if lq in set_cycle:
                    continue
                seen[lq] = 1
                toadd[lq] = toadd[q] +1
                ans += len(cycle) + toadd[lq]
                Q.append(lq)

print(ans)






