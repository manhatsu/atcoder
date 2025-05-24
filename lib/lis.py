# LIS: 最長増加部分列
# 与えられた数列の中で、順序を変えずに要素を取り出して作る部分列のうち、
# 増加列（各要素が前の要素より大きい）の中で最も長いもの
# O(NlogN)

from bisect import  bisect_left

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]
m0 = [1]
for a in A[1:]:
    if a > LIS[-1]:
        LIS.append(a)
    else:
        LIS[bisect_left(LIS, a)] = a
    m0.append(len(LIS))