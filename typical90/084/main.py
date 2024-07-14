N = int(input())
S = input()
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

#全l, rの組み合わせ
ret = N*(N-1)//2+N

'''
# NGの範囲見つける
i = 0
j = 0
num_ox = {'o':0, 'x':0}
num_ox[S[0]] = 1
ng_kukan = [] # 右開区間

endloop = False
while True:
    while (num_ox['o'] == 0) or (num_ox['x'] == 0):
        j += 1
        if j >= N:
            endloop = True
            break
        num_ox[S[j]] += 1

    if endloop:
        break
    ng_kukan.append((i, j))
    # iをjまで更新
    while (i < j):
        num_ox[S[i]] -= 1
        i += 1
    
# 最後のNG区間を追加
ng_kukan.append((i, j))

# print(ng_kukan)

# [i, j)の中の組み合わせはNGなので，retから引く
for (i, j) in ng_kukan:
    if (i+1) == j:
        ret -= 1
    else:
        ret -= (j-i)*(j-i-1) // 2 + (j-i)

print(ret)
'''

# ランレングス圧縮による解法
from itertools import groupby

T = [(k, list(g)) for k, g in groupby(S)]
# print(T)

for (_, t) in T:
    M = len(t)
    ret -= M*(M+1)//2

print(ret)
