import sys
input = sys.stdin.readline


def seq(n):
    dp = seq_init(n)
    dp = seq_fill(dp, n)
    return dp[n]


def seq_init(n):
    dp = [0, 1, 1, 1, 2, 2] + [0]*(n-5)
    return dp


def seq_fill(dp, n):
    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    return dp


t = int(input())
for _ in range(t):
    n = int(input())
    print(seq(n))