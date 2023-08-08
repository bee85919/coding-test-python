def solution(n):
    mat, val, y = [[0] * n for _ in range(n)], 1, 0
    while n > 0:
        for x in range(n): mat[y][x+y] = val; val += 1
        for x in range(1, n): mat[x+y][n-1+y] = val; val += 1
        for x in range(1, n): mat[n-1+y][n-1-x+y] = val; val += 1
        for x in range(1, n-1): mat[n-1-x+y][y] = val; val += 1
        y += 1; n -= 2
    return mat
