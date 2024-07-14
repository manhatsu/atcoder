N, Q = map(int, input().split())

posx_list = [i for i in range(1, N+1)][::-1]
posy_list = [0]*N
# print(posx_list)

nowx = posx_list[-1]
nowy = posy_list[-1]

D = {'R':0, 'L':1, 'U':2, 'D':3}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(Q):
    q, r = input().split()

    if int(q) == 1:
        didx = D[r]
        nowx += dx[didx]
        nowy += dy[didx]
        posx_list.append(nowx)
        posy_list.append(nowy)
        

    elif int(q) == 2:
        p = int(r)
        # print(posx_list)
        # print(posy_list)
        print(posx_list[-p], posy_list[-p])
