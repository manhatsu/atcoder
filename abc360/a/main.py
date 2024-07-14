S = input()
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

r = -1
m = -1
for i, s in enumerate(S):
    if s == 'R':
        r = i
    elif s == 'M':
        m = i

print('Yes' if r < m else 'No')


