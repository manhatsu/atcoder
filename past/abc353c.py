N = int(input())
A = list(map(int, input().split()))

MOD = 10**8 # 1e8にするとWAになった

A_sorted = sorted(A)
# print(A_sorted)

def is_ok(mid, i):
    return A_sorted[mid] + A_sorted[i] >= MOD

def binary_search(l, r, i):
    while (abs(r-l) > 1):
        mid = (l+r) // 2
        if is_ok(mid, i):
            r = mid
        else:
            l = mid
    return r
 
# 1e8で割り切れる個数
n_1e8 = 0
for i in range(N-1):
    r = binary_search(i, N, i)
    # print(r)
    # print('add', N-r)
    n_1e8 += N-r

# print(n_1e8)

print((N-1)*sum(A)-n_1e8*MOD)


