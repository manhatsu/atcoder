from itertools import combinations
# N = int(input())
H, W = map(int, input().split())
# A_list = list(map(int, input().split()))
F = []

for i in range(H):
    F.append(list(map(int, input().split())))

# print(F)


a = [i for i in range(H-1+W-1)]
# print(a)

C = set(combinations(a, W-1)) # 横移動するidx

ans = 0
for c in C:
    # print(c)
    ret = True
    nh = 0
    nw = 0
    seen = {F[0][0]}
    for i in range(H-1+W-1):
        if i in c: # 横移動
            nw += 1
        else:
            nh += 1
        # print('now:', nh, nw)
        if F[nh][nw] in seen:
            ret = False
            break
        seen.add(F[nh][nw])
    if ret:
        ans += 1

print(ans) 





