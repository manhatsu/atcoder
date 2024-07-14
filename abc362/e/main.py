
N = int(input())
A = list(map(int, input().split()))

from collections import deque

ans = [N] # 長さ1
Q = deque()
temp = 0
for i in range(N):
    for j in range(i+1, N):
        d = A[j]-A[i]
        Q.append((j, 2, d, A[j], 1))
        temp += 1
ans.append(temp)

print(Q)

endloop = False
for z in range(3, N+1):
    temp = 0
    next_dic = {}
    while Q:
        n, k, d, l, v = Q.popleft()
        for i, a in enumerate(A[n+1:]):
            if a == l+d:
                if (n+1+i, k+1, d, a) not in next_dic.keys():
                    next_dic[(n+1+i, k+1, d, a)] = v+1
                else:
                    next_dic[(n+1+i, k+1, d, a)] += v+1
    print(next_dic)
    for t, w in next_dic.items(): 
        temp += w
        Q.append((t[0], t[1], t[2], t[3], w))
    ans.append(temp)

print(*ans)







