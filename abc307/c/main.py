A = []
B = []
X = []

H, W = map(int, input().split())
for i in range(H):
    S = input()
    for j, s in enumerate(S):
        if s == '#':
            A.append((i, j))

H, W = map(int, input().split())
for i in range(H):
    S = input()
    for j, s in enumerate(S):
        if s == '#':
            B.append((i, j))

H, W = map(int, input().split())
for i in range(H):
    S = input()
    for j, s in enumerate(S):
        if s == '#':
            X.append((i, j))

maxha = max([h for h, _ in A])
minha = min([h for h, _ in A])
maxwa = max([w for _, w in A])
minwa = min([w for _, w in A])
maxhb = max([h for h, _ in B])
minhb = min([h for h, _ in B])
maxwb = max([w for _, w in B])
minwb = min([w for _, w in B])

ans = False
for i in range(-minha, 10-maxha):
    for j in range(-minwa, 10-maxwa):
        alpha = [(h+i, w+j) for h, w in A]
        for k in range(-minhb, 10-maxhb):
            for l in range(-minwb, 10-maxwb):
                beta = [(h+k, w+l) for h, w in B]
                gamma = set(alpha + beta)
                if gamma == set(X):
                    ans = True
                    break
            if ans:
                break
        if ans:
            break
    if ans:
        break

print('Yes' if ans else 'No')










