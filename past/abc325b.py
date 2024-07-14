
N = int(input())

W_list = [0]*24
for i in range(N):
    w, x = map(int, input().split())
    W_list[x] += w

sum = sum(W_list[0:18-9])
max = sum
# max_idx = 0
for i in range(24):
    sum += W_list[(i+9)%24]
    sum -= W_list[i%24]
    if sum > max:
        max = sum

print(max)
