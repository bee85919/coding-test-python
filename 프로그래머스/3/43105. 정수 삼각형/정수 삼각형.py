def solution(tri):
    for y in range(len(tri)-2,-1,-1):
        for x in range(y+1): 
            tri[y][x]+=max(tri[y+1][x],tri[y+1][x+1])
    return tri[0][0]
