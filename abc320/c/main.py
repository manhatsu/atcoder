from itertools import permutations
M = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
S = []
for i in range(3):
    s = input()
    S.append(s+s+s)

# print(S)

sel_order = list(permutations([i for i in range(3)]))

ret = 10000
for (x, y, z) in sel_order:
    s0 = S[x]
    s1 = S[y]
    s2 = S[z]
    for N in range(10):
        N = str(N)
        found = 0
        for i in range(len(s0)):
            if s0[i] == N:
                # print('found {} in idx {}'.format(N, i))
                found += 1
                break
        if found == 0:
            # print(N, 'not found in s1')
            continue
        for j in range(i+1, len(s1)):
            if s1[j] == N:
                found += 1
                break
        if found == 1:
            continue
        for k in range(j+1, len(s2)):
            if s2[k] == N:
                found += 1
                break
        if found == 2:
            continue
        ret = min(k, ret)

# print(ret)
print(ret if ret != 10000 else -1)






