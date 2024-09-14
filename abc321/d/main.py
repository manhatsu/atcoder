from bisect import bisect, bisect_left, bisect_right

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = sorted(B)

S = []
temp = 0
for b in B:
    temp += b
    S.append(temp)

ans = 0 
for a in A:
    if a >= P:
        ans += P*M
    else:
        bd = bisect_right(B, P-a)
        # print(bd)
        if bd == 0:
            ans += P*M
        else:
            ans += a*bd+S[bd-1]+P*(M-bd)
    # print('ans', ans)

print(ans)




