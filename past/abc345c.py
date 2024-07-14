S = input()

offset = ord('a')

D = [0]*26
for s in S:
    idx = ord(s)-offset
    D[idx] += 1

# print(D)

ret = 0
for d in D:
    if d != 0:
        ret += (sum(D) - d)*d
ret = ret // 2

if any({d > 1 for d in D}):
    ret += 1

print(ret)    
