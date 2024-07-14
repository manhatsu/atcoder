H, W = map(int, input().split())

F = []
for i in range(H):
    s = input()
    F.append(s)

key = 'snuke'
si = 0
sj = 0

d = [-1, 0, 1]

def searchkey(F, key): 
    for i in range(H):
        for j in range(W):
            if F[i][j] == key[0]:
                # print('found "s":', i, j)
                for di in d:
                    for dj in d:
                        idh = i
                        idw = j
                        # print('search axis', di, dj)
                        found = True
                        for k in range(1, len(key)):
                            idh += di
                            idw += dj
                            if (not 0 <= idh < H) or (not 0 <= idw < W):
                                # print('index {}, {} out of Field'.format(idh, idw))
                                found = False
                                break
                            # print('searching', idh, idw)
                            if F[idh][idw] != key[k]:
                                found = False
                                break
                            # print('found {}:'.format(key[k]), idh, idw)
                        if found:
                            return i, j, di, dj
    return None, None, None, None
                        
i, j, di, dj = searchkey(F, key)

if i != None:
    for k in range(len(key)):
        print(i+di*k+1, j+dj*k+1)
                            


