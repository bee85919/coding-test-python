n = int(input())
num = [int(input()) for _ in range(n)]


def check(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


for n in num:
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        elif check(n):
            print(n)
            break
        else:
            n += 1