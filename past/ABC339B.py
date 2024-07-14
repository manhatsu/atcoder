h, w, N = map(int, input().split())

field = [['.']*w for i in range(h)]
# print(field)

nowh = 0
noww = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 方向指定
d_idx = 0

for i in range(N):
    if field[nowh][noww] == '.':
        field[nowh][noww] = '#'
        d_idx += 1
        nowh = (nowh + dx[d_idx % 4]) % h
        noww = (noww + dy[d_idx % 4]) % w
    else:
        field[nowh][noww] = '.'
        d_idx -= 1
        nowh = (nowh + dx[d_idx % 4]) % h
        noww = (noww + dy[d_idx % 4]) % w

for i in range(h):
    print("".join(field[i]))