s = input()
t = input()

'''
alphabet = 'ABCDE'
neighbor_list = ['EB', 'AC', 'BD', 'CE', 'AD']

ret = False
ret1 = False
if (s[1] in neighbor_list[alphabet.index(s[0])]):
    ret = True
if (t[1] in neighbor_list[alphabet.index(t[0])]):
    ret1 = True

if ret == ret1:
    print('Yes')
else:
    print('No')
'''

ret = 0
ret1 = 0

diff1 = abs(ord(s[0]) - ord(s[1]))
if diff1 == 1 or diff1 == 4:
    ret = 1

diff2 = abs(ord(t[0]) - ord(t[1]))
if diff2 == 1 or diff2 == 4:
    ret1 = 1

print('Yes' if ret == ret1 else 'No')