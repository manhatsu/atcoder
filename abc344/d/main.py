T = input()
N = int(input())

A = [0]*N
S = [[]] # 0袋のときの空配列を入れておく
for i in range(N):
    Z = list(input().split())
    A[i] = int(Z[0])
    S.append(Z[1:])

# print(S)
inf = 10**9
dp = [[inf]*(N+1) for _ in range(len(T)+1)] # dp[t][n]: n袋目まで使ってTのt文字目まで合うときの最小コスト

for n in range(N+1):
    dp[0][n] = 0

for n in range(1, N+1):
    # print('use {} bags'.format(n))
    for t in range(len(T)+1): 
        # 一個前の時点でt文字目まで合っている状況を考える 
        # t=0のときは1文字も合っていない
        # ありえない状況の場合はスキップ
        if dp[t][n-1] == inf:
            continue
        # 何も選ばない場合，n-1袋目までの結果を引き継ぐ
        dp[t][n] = min(dp[t][n], dp[t][n-1])
        # 選んだほうがコストが小さくなる可能性を探索
        for s in S[n]: # n袋目の中の各文字列sに対して
            # print('s:', s)
            add = True
            # sの長さ分足すとTの長さを超える場合はNG
            if len(s) > len(T[t:]):
                add = False
            else:
                for i in range(len(s)):
                    if s[i] != T[t+i]:
                        add = False
            if not add: # sを選べない
                continue
            # print('add {}'.format(s))
            # sがTのt+1文字目からt+dt文字目まで一致する
            # 選ぶ（1円追加する）ことで，t+dt文字目まで合わせられる
            # 今までより小さい値になるときに更新
            dp[t+len(s)][n] = min(dp[t+len(s)][n], dp[t][n-1]+1)
            # print('dp[{}][{}]='.format(t+len(s), n), dp[t+len(s)][n])

# for t in range(len(T)+1):
    # print(*dp[t])
print(dp[len(T)][N] if dp[len(T)][N] != inf else -1)











