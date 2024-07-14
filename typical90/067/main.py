N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

eight_list = [1]
nine_list = [1]
temp0 = 1
temp1 = 1
for i in range(20):
    temp0 *= 8
    temp1 *= 9
    eight_list.append(temp0)
    nine_list.append(temp1)


def to9(str_num):
    if str_num == '0':
        return '0'
    num10 = 0
    for i in range(len(str_num)):
        num10 += int(str_num[len(str_num)-1-i])*eight_list[i]
    # print('10sinsuu', num10)
    j = len(nine_list)-1
    while True:
        if num10 < nine_list[j]:
            j -= 1
            if j < 0:
                break
        else:
            break

    # print('max keta in 9 sinsuu:', j)
    str_num9 = ''
    for k in range(j+1):
        digit = str(num10 // nine_list[j - k])
        # print('{} ketame in 9 sinsuu:'.format(j-k), digit)
        if digit == '8':
            str_num9 += '5'
        else:
            str_num9 += digit
        num10 = num10 % nine_list[j-k]
        # print('nokori in 10sinsuu:', num10)
    return str_num9

ret = str(N)
for i in range(K):
    ret = to9(ret)
    # print('changed to', ret)

print(ret)