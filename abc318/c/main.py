N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F = sorted(F)

G = []
for i in range(N):
    f = F.pop()
    if f >= (P/D):
        G.append(f)
    else:
        F.append(f)
        break

ans = P * (len(G) // D)
if len(G) % D != 0:
    nokori = len(G) % D
    kingaku = 0
    for g in G[-nokori:]:
        kingaku += g
    for i in range(min(D-nokori, len(F))):
        f = F.pop()
        kingaku += f
    if kingaku >= P:
        ans += P
    else:
        ans += kingaku

for f in F:
    ans += f

print(ans)    

