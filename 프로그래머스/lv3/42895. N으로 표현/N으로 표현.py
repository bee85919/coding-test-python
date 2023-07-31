def solution(n,num):
    
    stack = [set([int(str(n)*i)]) for i in range(1,9)] 
    
    if n == num: return 1    

    for i in range(1,len(stack)):
        for j in range(i):
            for x in stack[j]:
                for y in stack[i-j-1]: 
                    if y!=0: stack[i].update({x+y, x-y, x*y, x//y})
                    else: stack[i].add(x)
                    
        if num in stack[i]: return i+1

    return -1