S = input()
T = input()

# print(S)
t = T.lower()
if t[-1] == 'x':
    t = t[:-1]
# print(t)

now = 0
i = 0
ret = False
while True:
    if i >= len(S):
        break
    if t[now] == S[i]:
        # print(t[now], 'found in idx', i)
        now += 1
        if now == len(t):
            ret = True
            break
    i += 1

print('Yes' if ret else 'No')


