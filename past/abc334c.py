N, K = map(int, input().split())
A = list(map(int, input().split()))
# print(A)

J = A[::2]
I = A[1::2]
# print(I)
# print(J)

if len(I) == len(J):
    ans = sum([abs(i-j) for i, j in zip(I, J)])

else:
    J = J[1:]
    # print(I, J)
    ret = sum([abs(i-j) for i, j in zip(I, J)])
    ans = ret
    # print(ret)

    for k in range(0, K-1):
        isOdd = int((k) % 2)
        idx = (k) // 2
        if isOdd:
            # print('change {} to {}'.format(J[idx], A[k]))
            ret = ret - J[idx] + A[k]
        else:
            # print('change {} to {}'.format(I[idx], A[k]))
            ret = ret + I[idx] - A[k]

        # print(ret)
            
        if ret < ans:
            ans = ret

print(ans)