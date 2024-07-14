a, m, l, r = map(int, input().split())

if (l-a) % m == 0:
    k1 = (l-a) // m
else:
    k1 = (l-a) // m + 1

k2 = (r-a) // m

print(k2-k1+1)