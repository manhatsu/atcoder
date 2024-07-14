N = int(input())
X = []
Y = []
INF = 10**20

for i in range(N):
    x, y = map(int, input().split())
    X.append(x+10**9)
    Y.append(y+10**9)

X = sorted(X)
Y = sorted(Y)
# print(X)
# print(Y)

# 累積和
S_X = []
S_Y = []
tempx = 0
tempy = 0
for x in X:
    tempx += x
    S_X.append(tempx)
for y in Y:
    tempy += y
    S_Y.append(tempy)
# print('S_X', S_X)
ret_X = INF
ret_Y = INF
for i in range(N-1):
    if N >= 2*(i+1):
        a = X[i+1]
        b = Y[i+1]
    else:
        a = X[i]
        b = Y[i]
    D_X = -S_X[i]+(S_X[N-1]-S_X[i])-a*(N-2*(i+1))
    # print('D_X', D_X)
    D_Y = -S_Y[i]+(S_Y[N-1]-S_Y[i])-b*(N-2*(i+1))
    # print('D_Y', D_Y)
    ret_X = min(ret_X, D_X)
    ret_Y = min(ret_Y, D_Y)

# １点しかないとき
if N == 1:
    print(0)
else:
    print(ret_X+ret_Y)

# 1区間ずつ調べなくても，a or bがX or Yの中央値となれば良い
