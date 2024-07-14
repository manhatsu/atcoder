a, b, c = map(int, input().split())
# A_list = list(map(int, input().split()))

if a == 1:
    if c == 1:
        ret = False
    else:
        ret = True

else:
    if c ** b > a:
        ret = True
    else:
        ret = False

print('Yes' if ret else 'No')



