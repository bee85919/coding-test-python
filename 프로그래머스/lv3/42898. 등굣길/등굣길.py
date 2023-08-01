def solution(m, n, pd):
    
    pd, dp, dp[1][1] = [[q,p] for [p,q] in pd], [[0]*(m+1) for i in range(n+1)], 1

    for i in range(1, n+1):
        for j in range(1, m+1): 
            if [i,j] == [1,1]: continue
            if [i,j] in pd: dp[i][j] = 0 
            else: dp[i][j] = (dp[i-1][j] + dp[i][j-1])
            
    return dp[n][m] % 1000000007