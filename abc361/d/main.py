from collections import deque
N = int(input())
S = input()
T = input()

S += '..'
T += '..'

seen = dict()
seen[S] = 0

Q = deque()
Q.append(S)

while Q:
    q = Q.popleft()
    if q == T:
        break
    empty_idx = q.find('..')
    if empty_idx >= 2:
        for i in range(empty_idx-1):
            a = list(q)
            b = a.copy()
            b[i:i+2] = ['.', '.']
            b[empty_idx:empty_idx+2]  =a[i:i+2]
            r = ''.join(b)
            if r not in seen:
                seen[r] = seen[q] + 1
                Q.append(r)
    if empty_idx <= N-2:
        for i in range(empty_idx+2, N+1):
            a = list(q)
            b = a.copy()
            b[i:i+2] = ['.', '.']
            b[empty_idx:empty_idx+2]  =a[i:i+2]
            r = ''.join(b)
            if r not in seen:
                seen[r] = seen[q] + 1
                Q.append(r)

if T in seen:
    print(seen[T])
else:
    print(-1)