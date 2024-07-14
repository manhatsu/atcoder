from itertools import permutations
import math
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

F = []
for i in range(3):
    c, d, e = map(int, input().split())
    F.append(c)
    F.append(d)
    F.append(e)

W = []

# 横
for i in range(3):
    l = F[3*i]
    m = F[3*i+1]
    r = F[3*i+2]

    if l == m:
        W.append((3*i, 3*i+1, 3*i+2))
    elif l == r:
        W.append((3*i, 3*i+2, 3*i+1))
    elif m == r:
        W.append((3*i+1, 3*i+2, 3*i))

# 縦
for i in range(3):
    u = F[i]
    m = F[i+3]
    d = F[i+6]

    if u == m:
        W.append((i, i+3, i+6))
    elif u == d:
        W.append((i, i+6, i+3))
    elif m == d:
        W.append((i+3, i+6, i))

# 斜め
ul = F[0]
m = F[4]
dr = F[8]
ur = F[2]
dl = F[6]

if ul == m:
    W.append((0, 4, 8))
elif ul == dr:
    W.append((0, 8, 4))
elif m == dr:
    W.append((4, 8, 0))
if ur == m:
    W.append((2, 4, 6))
elif ur == dl:
    W.append((2, 6, 4))
elif m == dl:
    W.append((4, 6, 2))

combi_list = list(permutations([i for i in range(9)]))

ret = 0
for combi in combi_list:
    dict = {}
    for i in range(9):
        dict[combi[i]] = i
    isGakkari = False
    for (f,s,t) in W:
        if (dict[f] < dict[t]) and (dict[s] < dict[t]):
            isGakkari = True
            break
    if not isGakkari:
        ret += 1

print(ret / math.factorial(9))








