import math
N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

meanA = sum(A)/len(A)

left = 0
right = 0
for a in A:
    if a <= meanA:
        left += (int(meanA)-a)
    else:
        right += (a-(int(meanA)+1))

print(max(left, right))








