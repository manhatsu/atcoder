N = int(input())
S = input()
T = input()

nums = 0
numt = 0
for i in range(N):
    if S[i] == 'B':
        nums += 1
    if T[i] == 'B':
        numt += 1
if nums != numt:
    ans = -1

else:
    # N, K = map(int, input().split())
    # A_list = list(map(int, input().split()))
    S += '..'
    T += '..'

    asta_idx = N # .の左側

    def getDiff(S, T, idx): # 現在位置での相違度
        diff = 0
        for i in range(2):
            if S[idx+i] != T[idx+i]:
                if S[idx+i] != '.' and T[idx+i] != '.':
                    diff += 1
        return diff

    def getDiff1(S, T, idx, asta_idx): # ずらしたときの相違度
        diff = 0
        for i in range(2):
            if S[idx+i] != T[asta_idx+i]:
                if S[idx+i] != '.' and T[asta_idx+i] != '.':
                    diff += 1
        return diff

    # 移したときに相違度が一番小さく変化するものを選ぶ
    ans = 0
    while S != T:
        temp_dec = 0 # 減少する相違度
        temp_idx = -1
        for idx in range(N+1):
            # if idx%2 != 0:
                # continue
            if S[idx] == '.' or S[idx+1] == '.':
                continue
            dec_lev = getDiff(S, T, idx) - getDiff1(S, T, idx, asta_idx)
            # print('idx, dec_lev', idx, dec_lev)
            if temp_dec < dec_lev:
                temp_dec = dec_lev
                temp_idx = idx
        
        ans += 1
        if temp_dec == 0:
            break
        newS = ''
        # print(temp_idx)
        # print(temp_dec)
        for i, s in enumerate(S):
            if i == temp_idx or i == temp_idx+1:
                newS += '.'
            elif i == asta_idx:
                newS += S[temp_idx]
            elif i == asta_idx+1:
                newS += S[temp_idx+1]
            else:
                newS += s
        S = newS
        # print(S)
        asta_idx = temp_idx

print(ans)












