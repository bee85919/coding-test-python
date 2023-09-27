def solution(dist, rocks, n):
    
    rocks.sort()
    rocks.append(dist) 
    
    ans, L, R = 0, 1, dist
    
    while L <= R:
        
        mid, pre, cnt = (L+R)//2, 0, 0
        
        for rock in rocks:
            if rock-pre < mid: 
                cnt += 1
            else: 
                pre = rock
                
        if cnt > n: 
            R = mid - 1
        else: 
            ans = mid
            L = mid + 1

    return ans
