import itertools

N = int(input())
C = [[] for i in range(N)]
for i in range(N):
    A = list(map(int, input().split()))
    C[i] = A

# print(*C)

K = [[0]*N for i in range(N)]
M = int(input())
for i in range(M):
    x, y = map(int, input().split())
    K[x-1][y-1] = 1
    K[y-1][x-1] = 1

ans = 1000000
l = [i for i in range(N)]
# np.arangeだと遅い
for v in itertools.permutations(l):
    # print('candidate', v)
    ret = True
    temp = 0
    bef = -1
    for i, val in enumerate(v):
        if (bef != -1) and (K[bef][val] == 1):
            ret = False
            break
        temp += C[val][i]
        bef = val
        # print('temp +=', C[val][i])
    # print('time', temp)
    if ret:
        ans = min(temp, ans)

print(ans if ans != 1000000 else -1)