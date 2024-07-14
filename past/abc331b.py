N, S, M, L = map(int, input().split())

ret_list = [i*S + j*M + k*L for i in range(N // 6 + 2) for j in range(N // 8 + 2) for k in range(N // 12 + 2) if 6*i + 8*j + 12*k >= N] 

print(min(ret_list))