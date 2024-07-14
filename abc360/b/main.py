S, T = input().split()

ret = False
for w in range(1, len(S)):
    for c in range(1, w+1):
        s = ''
        for i in range(len(S)//w+1):
            substr = S[i*w:min(len(S), i*w+w)]
            if len(substr) >= c:
                s += substr[c-1]

        if s == T:
            ret = True
            break
    if ret:
        break

print('Yes' if ret else 'No')




