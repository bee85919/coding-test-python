from math import ceil
li = list(map(int, input().split(" ")))
A, B, V = li
H = V - A
X = A - B
print(ceil(H / X) + 1)