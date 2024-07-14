A, B = map(int, input().split())

if A == B:
    ret = -1
else:
    if A == 1:
        if B == 2:
            ret = 3
        else:
            ret = 2
    elif A == 2:
        if B == 1:
            ret = 3
        else:
            ret = 1
    else:
        if B == 1:
            ret = 2
        else:
            ret = 1

print(ret)