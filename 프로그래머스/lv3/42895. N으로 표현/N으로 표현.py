def solution(N,num):
    
    if N == num: return 1

    sta = [set([int(str(N) * i)]) for i in range(1, 9)]

    for i in range(1,len(sta)):
        
        for j in range(i):
            for a in sta[j]:
                for z in sta[i-j-1]: sta[i].update({a+z,a-z,a*z,a//z}) if z!=0 else sta[i].add(a)
                    
        if num in sta[i]: return i+1

    return -1  
