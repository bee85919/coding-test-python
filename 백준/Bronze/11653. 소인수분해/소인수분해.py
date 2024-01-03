import sys
input = sys.stdin.readline


def factorization(n):
    if n == 1:
        return 
    for i in range(2, n+1):
        if n%i == 0:
            print(i)
            return factorization(n//i)

n = int(input())
factorization(n)