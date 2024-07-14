N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

ret = 0
for i in range(N):
    s = input()
    if s == 'Takahashi':
        ret += 1

print(ret)


