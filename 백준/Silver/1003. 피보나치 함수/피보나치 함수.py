# import sys
# input = sys.stdin.readline


def feb(dp):
    for i in range(2, 41):
        dp[i] = dp[i-1] + dp[i-2]
    return dp


n = int(input())
lst = [int(input()) for _ in range(n)]


dp0 = 41*[0]
dp1 = 41*[0]
dp0[0] = 1
dp1[1] = 1
dp0 = feb(dp0)
dp1 = feb(dp1)


for l in lst: 
    print(dp0[l], dp1[l])