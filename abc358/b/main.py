N, A = map(int, input().split())
T = list(map(int, input().split()))

B = []
fin = 0
for t in T:
    begin = max(fin, t)
    B.append(begin)
    fin = begin+A

for b in B:
    print(b+A)
