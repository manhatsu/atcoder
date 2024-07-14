N, Q = map(int, input().split())
A = list(map(int, input().split()))

shift = 0
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1: # swap
        x -= 1
        y -= 1
        actx = (x-shift) % N
        acty = (y-shift) % N
        temp = A[actx]
        A[actx] = A[acty]
        A[acty] = temp
    elif t == 2: # shift
        shift += 1
    else: # print
        x -= 1
        actx = (x-shift) % N
        print(A[actx])







