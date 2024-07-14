
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

D = {}

for i in range(N):
    S = input()
    if S not in D:
        D[S] = 1
        print(i+1)





