N, L, R = map(int, input().split())

a_list = list(map(int, input().split()))

ret_list = []
for a in a_list:
    if a <= L:
        ret_list.append(L)
    elif a >= R:
        ret_list.append(R)
    else:
        ret_list.append(a)

print(*ret_list)
