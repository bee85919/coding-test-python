import sys
input = sys.stdin.readline


def dp(n):
    if n==0 or n==1: return 1
    lst = dp_init(n)
    lst = dp_fill(n, lst)
    return lst[n]


def dp_init(n):
    lst = (n+1)*[0]
    lst[0] = 1
    lst[1] = 1
    return lst


def dp_fill(n, lst):
    for i in range(2, n+1):
        lst[i] = (lst[i-1] + 2*lst[i-2]) % 10007
    return lst


n = int(input())
print(dp(n))