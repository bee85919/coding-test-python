import sys
input = sys.stdin.readline


def ch(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


di = {}
def dp(n, di):
    if n in di:
        return di[n]
    ch_n = ch(n)
    di[n] = ch_n
    return ch_n


m = int(input())
for _ in range(m):
    n = int(input())
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        elif dp(n, di):
            print(n)
            break
        else:
            n += 1