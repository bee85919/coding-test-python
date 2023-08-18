from collections import deque

def solution(rect, charX, charY, itemX, itemY):
    answer = 0
    field = [[-1] * 102 for _ in range(102)]
    
    # Double all coordinates and fill the field
    for r in rect:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] == -1: # Fill with 1 for border
                    field[i][j] = 1
                    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([charX * 2, charY * 2])
    visited = [[1] * 102 for _ in range(102)]
    visited[charX * 2][charY * 2] = 0
    
    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # Check if the next position is within the field and is a border
            if 0 <= nx < 102 and 0 <= ny < 102 and field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return answer
