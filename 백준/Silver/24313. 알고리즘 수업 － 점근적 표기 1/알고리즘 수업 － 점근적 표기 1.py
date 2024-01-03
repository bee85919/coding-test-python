import sys
input = sys.stdin.readline


a1, a0 = map(int, input().split(" "))
c = int(input())
n0 = int(input())


for n in range(n0, 101):
    fn = a1 * n + a0
    gn = c * n
    if fn > gn:
        print(0)
        break
else:
    print(1)