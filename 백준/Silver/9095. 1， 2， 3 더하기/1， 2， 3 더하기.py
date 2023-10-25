import sys
input = sys.stdin.readline


def dp_cal(dp, i): return dp[i-1] + dp[i-2] + dp[i-3]


T = int(input())
lst = [int(input()) for _ in range(T)]


dp = 11*[0]
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11): dp[i] = dp_cal(dp, i)


for l in lst: print(dp[l])