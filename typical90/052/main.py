N = int(input())

L = []
for i in range(N):
    l = sum(list(map(int, input().split())))
    L.append(l)

ret = 1
for l in L:
    ret *= l

print(ret % (10**9+7))


# A_list = list(map(int, input().split()))




