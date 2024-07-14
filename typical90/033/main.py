H, W = map(int, input().split())

def kiriage(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n // 2 + 1)

if (H == 1) or (W ==1): # コーナーケース
    print(H*W)
else:
    print(kiriage(H)*kiriage(W))