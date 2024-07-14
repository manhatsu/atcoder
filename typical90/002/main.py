N = int(input())

ans = []
for i in range(2**N):
    ret = True
    S = []
    J = []
    for j in range(N):
        if ((i >> j) & 1):
            S.append("(")
            J.append("(")
        else:
            if len(J) == 0:
                ret = False
                break
            w = J.pop()
            if w != "(":
                ret = False
                break
            S.append(")")
    if len(J) != 0:
        ret = False   

    if ret:
        ans.append("".join(S))

ans = sorted(ans)
for a in ans:
    print(a)