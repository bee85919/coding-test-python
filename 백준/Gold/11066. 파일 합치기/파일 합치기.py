import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    psum = [0]*(n+1)

    for i in range(1, n+1):
        psum[i] =  data[i-1]
        psum[i] += psum[i-1]
    
    dp = [[float('inf')]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0
    
    for i in range(2, n+1): # 길이
        for j in range(n-i+1): # 시작
            for k in range(j, j+i-1): # 순회 
                a = dp[j][j+i-1]
                b = dp[j][k] + dp[k+1][j+i-1] + psum[j+i] - psum[j]
                dp[j][j+i-1] = min(a, b)
                
    print(dp[0][n-1])