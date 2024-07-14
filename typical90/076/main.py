N = int(input())
A = list(map(int, input().split()))

B = A+A

ans = 'No'
whole = sum(A)

if whole % 10 == 0:
    ideal = whole // 10
    i, j = 0, 0
    temp = 0
    endloop = False
    ans = 'No'
    while i < N:
        while (temp < ideal):
            if j >= len(B):
                ans = 'No'
                endloop = True
                break
            temp += B[j]
            j += 1
        if endloop:
            break
        if temp == ideal:
            ans = 'Yes'
            break
        # tempがidealを超えたら，iを右にシフト
        temp -= B[i]
        i += 1

print(ans)









