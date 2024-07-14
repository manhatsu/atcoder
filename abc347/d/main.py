a, b, C = map(int, input().split())
# A_list = list(map(int, input().split()))

# Cの1が立っている個数を取得
c = C.bit_count()

# 最上位ビットを返す
def getHighestBitPos(M):
    if M == 0:
        return -1
    ans = 0
    while(M != 0):
        ans += 1
        M >>= 1
    return ans-1

# print(getHighestBitPos(C))

if c == 0:
    if a != b:
        ans = [-1]
    else:
        if a == 0:
            ans = [0, 0]
        else:
            X = ''
            for i in range(a):
                X += '1'
            ans = [int(X, 2), int(X, 2)]

elif (a+b-c) % 2 != 0:
    # 作れない
    ans = [-1]
else:
    # 1を重ねる個数k個
    k = (a+b-c) // 2
    if not(0<=k<=min(a, b)):
        # 作れない
        ans = [-1]
    else:
        # Cの1が立っている桁については，
        # a-k個まではXに1を立てて，残りには0を立てる
        rem_1 = a+b-2*k
        # Cの0が立っている桁については，k個までX, Yともに1を立てていく
        rem_0 = k
        X = ''
        Y = ''

        for i in range(getHighestBitPos(C)+1):
            if (C>>i & 1):
                if rem_1 > b-k:
                    X += '1'
                    Y += '0'
                    rem_1 -= 1
                else:
                    X += '0'
                    Y += '1'
            else:
                if rem_0 > 0:
                    X += '1'
                    Y += '1'
                    rem_0 -= 1
                else:
                    X += '0'
                    Y += '0'
        # 使うべき1がまだ残っている場合は使う
        while (rem_0 > 0):
            X += '1'
            Y += '1'
            rem_0 -= 1
        # XかYの最上位ビットが61桁以上の場合NG
        if getHighestBitPos(int(X[::-1], 2)) >= 60 or getHighestBitPos(int(Y[::-1], 2)) >= 60:
            ans = [-1]
        else:
            # X, Yを反転して2進数変換
            ans = [int(X[::-1], 2), int(Y[::-1], 2)]

print(*ans)




