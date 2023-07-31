def solution(triangle):
    for y in range(len(triangle)-2,-1,-1):
        for x in range(y+1): triangle[y][x]+=max(triangle[y+1][x],triangle[y+1][x+1])
    return triangle[0][0]
