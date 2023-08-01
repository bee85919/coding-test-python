def solution(house):
    
    def rob(house):
        
        if not house: return 0    
        if len(house) <= 2: return max(house)    
    
        dp, dp[0], dp[1] = [0]*len(house), house[0], max(house[0], house[1])        
        for i in range(2, len(house)): dp[i] = max(dp[i-2]+house[i],dp[i-1])    
        return dp[-1]
    
    return max(rob(house[1:]), rob(house[:-1]))