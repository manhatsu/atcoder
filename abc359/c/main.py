sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
# A_list = list(map(int, input().split()))

nx = sx
ny = sy
cost = 0

cost += abs(sy-ty)
ny = ty

if sx != tx:
    # スタートポジション
    if (sx+sy)% 2 == 0:
        startpos = 'l'
    else:
        startpos = 'r'
    # 行く方向
    if sx > tx: # 左
        if startpos == 'l':
            nx = sx - abs(sy - ty)
        else:
            nx = sx - abs(sy - ty) - 1
        if nx > tx:
            cost += (nx - tx + 1) // 2
    else:
        # print('going to right')
        if startpos == 'l':
            nx = sx + abs(sy - ty) + 1
        else:
            nx = sx + abs(sy - ty)
        # print(nx)
        if nx < tx:
            cost += (tx - nx + 1) // 2

print(cost)










