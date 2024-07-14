# from collections import deque

N = int(input())
A = list(map(int, input().split()))

CNT = N
Q = []
for i in range(N):
    Q.append(A[i])
    while len(Q)>=2:
        now = Q.pop()
        prev = Q.pop()
        if now == prev:
            now += 1
            Q.append(now)
            CNT -= 1
        else:
            Q.append(prev)
            Q.append(now)
            break
    
print(CNT)