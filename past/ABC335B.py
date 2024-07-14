N = int(input())

ans = [[i, j, k] for i in range(N+1) for j in range(0, N+1-i) for k in range(0, N+1-i-j)]

for a in ans:
    print(*a)
