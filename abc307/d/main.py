
N = int(input())
S = input()

ans = ''
temp = []
phase = 0
for s in S:
    if s == '(':
        phase = 1
        temp.append('(')
    elif phase == 0:
        ans += s
    else:
        if s == ')':
            temp.pop()
            if len(temp) == 0:
                phase = 0
        else:
            temp[-1] += s

if len(temp) > 0:
    ans += ''.join(temp)

print(ans)







