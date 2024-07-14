L, R = map(int, input().split())
# A_list = list(map(int, input().split()))

def getHighestBitPos(n):
    if n == 0:
        return 0
    ans = -1
    while n != 0:
        n >>= 1
        ans += 1
    return ans-1

ans = []
l = L
r = 0

while r != R:
    if l == 0:
        j = getHighestBitPos(R)
        r = 2**j
    else:     
        for i in range(61):
            if (l>>i & 1):
                break
        
        j = getHighestBitPos(R-l)
        r = l+2**min(i, j)
    ans.append((l, r))
    l = r

print(len(ans))
for a in ans:
    print(*a)

