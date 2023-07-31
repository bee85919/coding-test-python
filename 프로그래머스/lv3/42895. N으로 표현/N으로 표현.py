def solution(n,num):   
    
    if n == num: return 1  

    def cal(x,y): return {x+y, x-y, x*y, x//y if y else x}

    s = [{int(str(n)*i)} for i in range(1,8+1)]
    n = len(s)
    for i in range(n):
        for j in range(i):
            for row in s[j]:
                for col in s[i-1-j]: s[i].update(cal(col,row))    
        if num in s[i]: return i+1
    
    return -1