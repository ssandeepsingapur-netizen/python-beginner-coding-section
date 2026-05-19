from itertools import product

A = list(map(int ,input().split()))
B = list(map(int ,input().split()))

a  = list(A)
b = list(B)

print(*product(a,b))