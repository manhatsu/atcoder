# from decimal import Decimal
# floatだとWA, DecimalだとPyPyはTLE, Python3ならAC

N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

S = []
for i in range(N):
    # A, B =input().split()
    A, B = map(int, input().split())
    S.append((-A*10**100//(A+B), i))

S = sorted(S)

print(*[i+1 for s, i in S])
