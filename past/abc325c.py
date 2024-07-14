from collections import deque

H, W = map(int, input().split())

F = [[] for _ in range(H)]
for i in range(H):
    S = input()
    F[i] = S

seen = [[0]*W for _ in range(H)]


dh = [-1, -1, -1, 0, 0, 1, 1, 1]
dw = [-1, 0, 1, -1, 1, -1, 0, 1]

ret = 0
for i in range(H):
    for j in range(W):
        if (F[i][j] == '.') or (seen[i][j] == 1):
             continue
        else:
            ret += 1
            Q = deque()
            Q.append((i, j))
            while Q:
                nowh, noww = Q.popleft()
                for k in range(8):
                        sidh = nowh+dh[k]
                        sidw = noww+dw[k]
                        if (0 <= sidh < H) and (0 <= sidw < W) and (F[sidh][sidw] == '#') and (seen[sidh][sidw] == 0):
                                seen[sidh][sidw] = 1
                                Q.append((sidh, sidw))
print(ret)



