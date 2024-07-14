A, B = map(int, input().split())
# A_list = list(map(int, input().split()))

def yuc(A, B):
    if A % B == 0:
        return B
    return yuc(B, A%B)

gcf = yuc(A, B)
ret = A * B // gcf

print(ret if ret <= 1e18 else 'Large')



