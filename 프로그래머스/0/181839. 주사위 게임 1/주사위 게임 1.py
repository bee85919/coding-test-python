def solution(a, b):
    d1 = a % 2
    d2 = b % 2    
    if  d1 == 1 and d2 == 1:
        return a**2 + b**2
    elif d1 == 1 or d2 == 1:
        return 2 * (a + b)
    else: 
        return  abs(a - b)