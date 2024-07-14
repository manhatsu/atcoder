p = []
for i in range(3):
    x, y = map(int, input().split())
    p.append([x, y])

d12 = (p[0][0] - p[1][0]) ** 2 + (p[0][1] - p[1][1]) ** 2
d13 = (p[0][0] - p[2][0]) ** 2 + (p[0][1] - p[2][1]) ** 2
d23 = (p[1][0] - p[2][0]) ** 2 + (p[1][1] - p[2][1]) ** 2

ans = (d12 + d13 == d23) or (d12 + d23 == d13) or (d13 + d23 == d12)

print('Yes' if ans else 'No')



