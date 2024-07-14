N = int(input())

L = []
R = []

for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

'''
zip_list = zip(L, R)
zip_s = sorted(zip_list)
L, R = zip(*zip_s)
L = list(L)
R = list(R)
'''
L = sorted(L)
R = sorted(R)

# L = [x for x, _ in sorted(zip(L, R))]
# R = [x for _, x in sorted(zip(L, R))]

# print(L)
# print(R)

l = 0
r = 0
now = 0
kasanari = 0
sum = 0
while l < N:
    if L[l] <= R[r]:
        kasanari += 1
        l += 1
        sum += kasanari - 1
    else:
        kasanari -= 1
        r += 1

print(sum)

        
