# from icecream import ic

N, X = map(int, input().split())

T = []

for _ in range(N):
    a, b = map(int, input().split())
    T.append((a, b))

B = 1
for a, b in T:
    for i in range(b):
        B |= B << a

    # ic(bin(B))

ret = (B >> X) & 1
# ic(ret)



print('Yes' if ret else 'No')





