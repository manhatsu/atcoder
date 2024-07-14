N = int(input())
S = input()
# print(S)

'''
D  = [[] for _ in range(26)]
for i, s in enumerate(S):
    idx = ord(s) - ord('a')
    D[idx].append(i)
    '''

order_bef = 'abcdefghijklmnopqrstuvwxyz'
order = [l for l in order_bef]


Q = int(input())

for _ in range(Q):
    c, d = input().split()
    for i, l in enumerate(order):
        if l == c:
            order[i] = d
        
    # print(order)

T = []
for s in S:
    for i, l in enumerate(order_bef):
        if s == l:
            T.append(order[i])
            continue

print(''.join(T))