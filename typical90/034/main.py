import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))

i, j = 0, 0
nunique = 0
dic = {}

max_idx = [0]*N

while j < N:
    # if nunique > K:
        # print('error: nunique exceeded K')
        # sys.exit()
    if (A[j] in dic):
        dic[A[j]] += 1
        j += 1
    else:
        if nunique == K:
            # print('max idx for {} is {}'.format(i, j-1))
            max_idx[i] = j-1
            dic[A[i]] -= 1
            if dic[A[i]] == 0:
                _ = dic.pop(A[i])
                # print('{} removed from series'.format(A[i]))
                nunique -= 1
            i += 1
        else:
            # print('Add {} to dic'.format(A[j]))
            nunique += 1
            dic[A[j]] = 1
            j += 1
    # print('dic:', dic)

for rem in range(i, N):
    # print('max_idx[{}:] is {}'.format(i, j-1))
    max_idx[rem] = j-1

ret = 0
for i, v in enumerate(max_idx):
    ret = max((v-i+1, ret))

print(ret)

# dicに各値の出てきた回数を積算するのがポイント
        




