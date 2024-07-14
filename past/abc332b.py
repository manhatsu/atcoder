K, G, M = map(int, input().split())

g = 0
m = 0


for i in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        move = min(m, G-g)
        m -= move
        g += move
    # print(g, m)

print(g, m)
