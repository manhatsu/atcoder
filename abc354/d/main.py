a, b, c, d = map(int, input().split())
# A_list = list(map(int, input().split()))

od = [2, 1, 0, 1]
ev = [1, 2, 1, 0]

# 端っこだけ除いて考える
ans = 0
y1 = ((d-d%2) - (b+b%2)) // 2 + d%2
y2 = ((d-d%2) - (b+b%2)) // 2 + b%2
for i in range(4):
    if a%4 == 0:
        x = x = ((c-c%4)-a) // 4 + (c%4 > i)
    else:
        x = ((c-c%4) - (a+(4-a%4))) // 4 + (c%4 > i) + ((a%4 != 0) and (a%4 <= i))
    # print('x, ,y1, y2', x, y1, y2)
    ans += x*y1*od[i] + x*y2*ev[i]

print(ans)




