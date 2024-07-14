F = []
for i in range(9):
    F.append(input())

# 複雑な条件で分岐しなくても，setに入れて重複カウントすれば良い
# count = 0
'''
for h in range(9):
    for w in range(9):
        # print('h, w', h, w)
        if F[h][w] == '#':
            # 同じhに#があるか見る
            for lw in range(w+1, 9):
                if F[h][lw] != '#':
                    continue
                h2 = h+lw-w
                if h2<0 or h2>=9:
                        continue
                if F[h2][w] == '#' and F[h2][lw] == '#':
                    # print('found suihei square')
                    count += 1
            # h+1行目以降を探索
            for h1 in range(h+1, 9):
                 for w1 in range(9):
                        if F[h1][w1] != '#':
                            continue
                        if w1 == w:
                            continue
                        if w1 > w:
                            h2 = h+w1-w
                            w2 = w-(h1-h)
                            h3 = h1+w1-w
                            w3 = w1-(h1-h)
                        else: # w1<w
                            h2 = h+w-w1
                            w2 = w+h1-h
                            h3 = h1+w-w1
                            w3 = w1+h1-h
                        # (h1, w1)よりも下の領域から2点見つける
                        if 0<=h2<9 and 0<=h3<9 and 0<=w2<9 and 0<=w3<9:
                             if (h1<h2 and h1<h3) or (h1==h2 and w1<w2 and h1<h3) or (h1<h2 and h1==h3 and w1<w3):
                                if F[h2][w2] == '#' and F[h3][w3] == '#':
                                    # print('found naname square')
                                    count += 1 
'''
square_set = set()
def isValid(h, w):
    return (0<=h<9 and 0<=w<9 and F[h][w] == '#')
for h0 in range(9):
    for w0 in range(9):
        if F[h0][w0] == '#':
            for dh in range(-8, 9):
                for dw in range(-8, 9):
                    if dh==0 and dw==0:
                        continue
                    h1 = h0+dh
                    w1 = w0+dw
                    h2 = h0+dw
                    w2 = w0-dh
                    h3 = h1+dw
                    w3 = w1-dh
                    if isValid(h1, w1) and isValid(h2, w2) and isValid(h3, w3):
                        square = tuple(sorted(((h0, w0), (h1, w1), (h2, w2), (h3, w3))))
                        # sortedすると勝手にリスト化される！
                        # print(square)

                        if square in square_set:
                            continue
                        else:
                            # setに追加できるのはtuple: list, dictは不可
                            square_set.add(square)
# print(square_set)
print(len(square_set))



                




