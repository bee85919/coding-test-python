import sys
input = sys.stdin.readline


def create_set(k):
    return {input().strip() for _ in range(k)}


def myprint(s):
    print(len(s))
    for name in s:
        print(name)

n, m = map(int, input().split())
set_n = create_set(n)
set_m = create_set(m)


myprint(sorted(set_n & set_m))