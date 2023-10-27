import sys
input = sys.stdin.readline


def make_dp(n): 
    dp = (n+1)*[0]
    return dp


def init_dp(dp, n): 
    dp[1] = 1
    if n > 1: 
        dp[2] = 2
    return dp


def fill_dp(dp, n):
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    return dp


n = int(input())
dp = make_dp(n)
dp = init_dp(dp, n)
dp = fill_dp(dp, n)
print(dp[n])