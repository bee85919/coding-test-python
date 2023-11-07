def init(n, time):
    return min(time), max(time)*n


def bs(left, right, time):
    mid = (left+right)//2
    return sum(mid//t for t in time), mid
        
        
def calc(n, t, left, right, mid):
    if t >= n: 
        right = mid
    else: 
        left = mid+1
    return left, right


def solution(n, time):    
    left, right = init(n, time) 
    while left < right:
        t, mid = bs(left, right, time)
        left, right = calc(n, t, left, right, mid)
    return left