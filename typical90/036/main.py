N, Q = map(int, input().split())

X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x+y)
    Y.append(x-y)

minX = min(X)
maxX = max(X)
minY = min(Y)
maxY = max(Y)

for _ in range(Q):
    q = int(input())
    q -= 1
    ans = max(abs(X[q]-minX), abs(X[q]-maxX), abs(Y[q]-minY), abs(Y[q]-maxY))
    print(ans)



