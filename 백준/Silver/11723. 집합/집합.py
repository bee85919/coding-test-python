import sys
input = sys.stdin.readline
sys.setrecursionlimit(9999)


def calc(op, s, x):
    if op == "add":
        return s | (1 << x)
    elif op == "remove":
        return s & ~(1 << x)
    elif op == "check":
        return 1 if (s & (1 << x)) else 0
    elif op == "toggle":
        return s ^ (1 << x)
    elif op == "all":
        return (1 << 21) - 2
    elif op == "empty":
        return 0
    else:
        return s

    
s = 0
n = int(input())


for _ in range(n):
    op, *num = input().split()
    x = int(num[0]) if num else None

    if op == "check":
        print(calc(op, s, x))
    else:
        s = calc(op, s, x)