N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
added = False
for i, a in enumerate(A):
    if i == K:
        added = True
        ans.append(X)
    ans.append(a)
if not added:
    ans.append(X)

print(*ans)







