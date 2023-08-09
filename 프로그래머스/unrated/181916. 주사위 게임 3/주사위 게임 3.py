from collections import Counter


def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = Counter(dice)
    most = counts.most_common()

    if most[0][1] == 4: 
        return 1111 * most[0][0]
    
    elif most[0][1] == 3: 
        return (10*most[0][0] + most[1][0]) ** 2
    
    elif most[0][1] == most[1][1] == 2: 
        return (most[0][0] + most[1][0]) * abs(most[0][0] - most[1][0])
    
    elif most[0][1] == 2: 
        return most[1][0] * most[2][0]
    
    else: 
        return min(dice)